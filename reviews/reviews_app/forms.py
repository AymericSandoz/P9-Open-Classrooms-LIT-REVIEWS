from django import forms

from . import models
from django.core.validators import MinValueValidator, MaxValueValidator


class PhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'caption']


class TicketForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'content']


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(6)],  # Crée des choix de 0 à 5
        widget=forms.RadioSelect,
        initial=2
    )
    class Meta:
        model = models.Review
        fields = ['content']


class CombinedForm(forms.ModelForm):
    class Meta:
        model = models.Ticket
        fields = ['title', 'content', 'photo']  # Champs de Ticket

    # Ajoutez les champs de Review
    review_title = forms.CharField(max_length=128)
    review_content = forms.CharField(max_length=8192)
    review_rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(6)],  # Crée des choix de 0 à 5
        widget=forms.RadioSelect,
        initial=2
    )