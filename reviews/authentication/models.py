from django.contrib.auth.models import AbstractUser
from django.db import models
from reviews_app.models import Follow


class User(AbstractUser):

    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = (
        (CREATOR, 'Créateur'),
        (SUBSCRIBER, 'Abonné'),
    )
    role = models.CharField(
        max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle')

    def is_followed_by(self, user):
        return Follow.objects.filter(follower=user, following=self).exists()
