from django.conf import settings
from django.db import models


def upload_statuses_image(instance, filename):
    return "updates/{users}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


# Create your models here.
class Statuses(models.Model):  # fb status, social media posts, etc.
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # users to post content
    content = models.TextField(
        null=True, blank=True
    )  # content still posted if blank and raises no error
    image = models.ImageField(upload_to=upload_statuses_image, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.content)[:50]  # content up to 50 chars

