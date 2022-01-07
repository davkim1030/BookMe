from django.contrib.auth.models import User as DjangoUser
from django.db import models


class User(DjangoUser):
    pass


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    start_datetime = models.DateTimeField(null=False)
    end_datetime = models.DateTimeField(null=False)
    title = models.CharField(max_length=100, null=False)
    request_comment = models.TextField(null=True)
