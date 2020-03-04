from django.db import models


class Document(models.Model):
    name = models.CharField(default="",
                            blank=True,
                            max_length=25
                            )
    file = models.FileField()
