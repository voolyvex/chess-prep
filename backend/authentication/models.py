from django.db import models
from django.contrib.auth.models import AbstractUser
from pgn.models import Pgn


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_coach = models.BooleanField('coach status', default=False)
    my_games = models.ManyToManyField(Pgn, related_name='user_mygames')
    favorites = models.ManyToManyField(Pgn, related_name='user_favorites')
    assigned = models.ManyToManyField(Pgn, related_name='user_assigned')
 