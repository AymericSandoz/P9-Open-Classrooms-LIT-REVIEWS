from django.db import models
from django.conf import settings
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator


class Photo(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length=128, blank=True)
    uploader = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    IMAGE_MAX_SIZE = (800, 800)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Ticket(models.Model):
    photo = models.ForeignKey(
        Photo, null=True, on_delete=models.SET_NULL, blank=True, verbose_name="Image"
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="auteur"
    )
    content = models.TextField(max_length=150, verbose_name="Description")
    title = models.CharField(max_length=80, verbose_name="Titre")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="date de création")

    def get_class_name(self):
        return self.__class__.__name__


class Review(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Auteur"
    )
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, verbose_name="Ticket")
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)], default=2, verbose_name="Note"
    )
    title = models.CharField(max_length=80, verbose_name="Titre")
    content = models.CharField(
        max_length=150, blank=True, verbose_name="Commentaire")
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name="Date de création")

    def get_class_name(self):
        return self.__class__.__name__


class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='follower', on_delete=models.CASCADE)
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='following', on_delete=models.CASCADE)

    # class Meta:
    #     # ensures we don't get multiple UserFollows instances
    #     # for unique user-user_followed pairs
    #     unique_together = ('user', 'followed_user', )


class Block(models.Model):
    blocker = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='blocker', on_delete=models.CASCADE)
    blocked = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='blocked', on_delete=models.CASCADE)
