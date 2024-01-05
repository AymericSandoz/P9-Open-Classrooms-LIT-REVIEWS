from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from . import forms, models
from django.shortcuts import get_object_or_404
from django.forms import formset_factory
from django.db.models import Q
from authentication.models import User
from itertools import chain
from django.db.models import CharField, Value, BooleanField


@login_required
def home(request):
    followed_users_ids = list(models.Follow.objects.filter(
        follower=request.user).values_list('following__id', flat=True))
    # recup la liste des users qui m'ont bloqué
    blocked_users_ids = list(models.Block.objects.filter(
        blocked=request.user).values_list('blocker__id', flat=True))
    # retirer de la liste des users que je follow ceux qui m'ont bloqué
    for blocked_user_id in blocked_users_ids:
        if blocked_user_id in followed_users_ids:
            followed_users_ids.remove(blocked_user_id)

    followed_users_ids.append(request.user.id)

    followed_users = User.objects.filter(
        id__in=followed_users_ids)
    reviews = models.Review.objects.filter(author__in=followed_users)
    tickets = models.Ticket.objects.filter(author__in=followed_users)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )

    print(tickets)
    for ticket in tickets:
        print(ticket.title)
    return render(request, 'reviews_app/home.html', context={'posts': posts})


@login_required
@permission_required('blog.add_photo', raise_exception=True)
def photo_upload(request):
    form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            # set the uploader to the user before saving the model
            photo.uploader = request.user
            # now we can save
            photo.save()
            return redirect('home')
    return render(request, 'reviews_app/photo_upload.html', context={'form': form})


@login_required
def blog_and_photo_upload(request):
    blog_form = forms.BlogForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        blog_form = forms.BlogForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([blog_form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            blog = blog_form.save(commit=False)
            blog.author = request.user
            blog.photo = photo
            blog.save()
            return redirect('home')
    context = {
        'blog_form': blog_form,
        'photo_form': photo_form,
    }
    return render(request, 'reviews_app/create_ticket.html', context=context)


@login_required
def view_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'reviews_app/view_blog.html', {'blog': blog})


def edit_blog(request, blog_id):
    blog = get_object_or_404(models.Blog, id=blog_id)
    edit_form = forms.BlogForm(instance=blog)
    delete_form = forms.DeleteBlogForm()
    if request.method == 'POST':
        if 'edit_blog' in request.POST:
            edit_form = forms.BlogForm(request.POST, instance=blog)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
            if 'delete_blog' in request.POST:
                delete_form = forms.DeleteBlogForm(request.POST)
                if delete_form.is_valid():
                    blog.delete()
                    return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reviews_app/edit_blog.html', context=context)


@login_required
def create_multiple_photos(request):
    PhotoFormSet = formset_factory(forms.PhotoForm, extra=5)
    formset = PhotoFormSet()
    if request.method == 'POST':
        formset = PhotoFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    photo = form.save(commit=False)
                    photo.uploader = request.user
                    photo.save()
            return redirect('home')
    return render(request, 'reviews_app/create_multiple_photos.html', {'formset': formset})


@login_required
def create_ticket(request):
    form = forms.TicketForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()
            return redirect('home')
    return render(request, 'reviews_app/create_ticket.html', context={'form': form, 'photo_form': photo_form})


@login_required
def create_review(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.ReviewForm()
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    return render(request, 'reviews_app/create_review.html', context={'form': form, 'ticket': ticket})


@login_required
def create_review_and_ticket(request):
    form = forms.CombinedForm()
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.CombinedForm(request.POST)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()

            review = models.Review()
            review.author = request.user
            review.ticket = ticket
            review.title = form.cleaned_data['review_title']
            review.content = form.cleaned_data['review_content']
            review.rating = form.cleaned_data['review_rating']
            review.save()

            return redirect('home')

    context = {
        'form': form,
        'photo_form': photo_form
    }
    return render(request, 'reviews_app/create_review_and_ticket.html', context=context)


@login_required
def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    form = forms.TicketForm(instance=ticket)
    photo_form = forms.PhotoForm()
    if request.method == 'POST':
        form = forms.TicketForm(request.POST, instance=ticket)
        photo_form = forms.PhotoForm(request.POST, request.FILES)
        if all([form.is_valid(), photo_form.is_valid()]):
            photo = photo_form.save(commit=False)
            photo.uploader = request.user
            photo.save()
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.photo = photo
            ticket.save()
            return redirect('home')
    return render(request, 'reviews_app/edit_ticket.html', context={'form': form, 'photo_form': photo_form, 'ticket': ticket})


@login_required
def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    ticket.delete()
    return redirect('view_user_posts')


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    ticket = review.ticket
    form = forms.ReviewForm(instance=review)
    if request.method == 'POST':
        form = forms.ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'reviews_app/edit_review.html', context={'form': form, 'review': review, 'ticket': ticket})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(models.Review, id=review_id)
    review.delete()
    return redirect('view_user_posts')


# @login_required
# def search_and_view_follows(request):
#     query = request.GET.get('search')
#     all_users = User.objects.all()
#     users = None
#     if query:
#         users = all_users.filter(Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query))

#     followers = models.Follow.objects.filter(follower=request.user)
#     following = models.Follow.objects.filter(following=request.user)

#     return render(request, 'reviews_app/search_and_view_follows.html', context={'users': users, 'followers': followers, 'following': following})


@login_required
def search_and_view_follows(request):
    query = request.GET.get('search')
    all_users = User.objects.all()
    users = None
    if query:
        following_users = models.Follow.objects.filter(
            follower=request.user).values_list('following', flat=True)
        users = all_users.filter(Q(username__icontains=query) & ~Q(
            id__in=following_users) & ~Q(id=request.user.id))

    followers = models.Follow.objects.filter(follower=request.user)
    followings = models.Follow.objects.filter(following=request.user)
    following_users_ids = list(models.Follow.objects.filter(
        follower=request.user).values_list('following', flat=True))

    blocked_users_ids = list(models.Block.objects.filter(
        blocker=request.user).values_list('blocked', flat=True))
    print(following_users_ids)

    return render(request, 'reviews_app/search_and_view_follows.html', context={'users': users, 'followers': followers, 'followings': followings, 'following_users_ids': following_users_ids, 'query': query, 'blocked_users_ids': blocked_users_ids}
                  )


@login_required
def follow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    follow = models.Follow(follower=request.user, following=user)
    follow.save()
    return redirect('search_and_view_follows')


@login_required
def unfollow_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    follow = models.Follow.objects.filter(
        follower=request.user, following=user)
    follow.delete()
    return redirect('search_and_view_follows')


@login_required
def block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    block = models.Block(blocker=request.user, blocked=user)
    block.save()
    return redirect('search_and_view_follows')


@login_required
def unblock_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    block = models.Block.objects.filter(
        blocker=request.user, blocked=user)
    block.delete()
    return redirect('search_and_view_follows')


@login_required
def view_user_posts(request):
    tickets = models.Ticket.objects.filter(author=request.user)
    reviews = models.Review.objects.filter(author=request.user)
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))

    posts = sorted(
        chain(reviews, tickets),
        key=lambda post: post.date_created,
        reverse=True
    )
    return render(request, 'reviews_app/personnal_posts.html', context={'posts': posts})
