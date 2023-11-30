from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER_ROLES = [
        ('LEV_OPERATOR', 'Level Operator'),
        ('LEV_ENGINEER', 'Level Engineer'),
        ('LEV_MANAGER', 'Level Manager'),
        ('OWNER', 'Owner'),
    ]

    role = models.CharField(choices=USER_ROLES, max_length=20, default='LEV_MANAGER')

    def __str__(self):
        return self.username