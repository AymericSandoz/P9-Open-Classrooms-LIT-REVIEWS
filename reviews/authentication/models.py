from django.contrib.auth.models import AbstractUser
from django.db import models
from reviews_app.models import Follow


class User(AbstractUser):

    def is_followed_by(self, user):
        return Follow.objects.filter(follower=user, following=self).exists()
