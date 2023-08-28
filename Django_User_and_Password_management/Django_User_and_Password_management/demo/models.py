from django.db import models
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(max_length=FIRST_NAME_MAX_LENGTH,)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, primary_key=True,)
