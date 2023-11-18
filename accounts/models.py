from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Role(models.Model):
    name = models.CharField(max_length=36)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.role.name

