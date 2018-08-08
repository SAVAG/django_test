from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models

from django_tutorial.dicts.models import Gender, Interest


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    fb_id = models.CharField(max_length=128, null=True, blank=True)
    age = models.PositiveIntegerField(validators=[MinValueValidator(16)], null=True)
    gender = models.ForeignKey(
        Gender,
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    interests = models.ManyToManyField(Interest)

    class Meta:
        db_table = "profiles"
        managed = True

    def __str__(self):

        return self.user.username
