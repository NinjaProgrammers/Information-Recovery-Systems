from django.db import models


# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "documents"

    def __str__(self):
        return self.name
