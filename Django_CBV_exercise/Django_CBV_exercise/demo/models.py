from django.db import models


class Books(models.Model):
    TITLE_MAX_LENGTH = 40
    AUTHOR_MAX_LENGTH = 40

    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    author = models.CharField(max_length=AUTHOR_MAX_LENGTH)
