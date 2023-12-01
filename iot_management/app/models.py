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
    

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    telemetry_data = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
    

class TelemetryData(models.Model):
    device_id = models.IntegerField(primary_key=True)
    timestamp = models.DateTimeField()
    value = models.FloatField()

    class Meta:
        db_table = 'telemetry_data'