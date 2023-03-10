from django.db import models
from django.contrib.auth.models import User
from checkout.models import BaseOrderInfo


class UserProfile(BaseOrderInfo):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username
