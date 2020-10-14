import json
from django.conf import settings
from django.db import models

from django.core.serializers import serialize

# Create your models here.
def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize(self):
    #     qs = self
    #     return serialize("json", qs, fields=("user", "content", "image"))

    # inefficient
    # def serialize(self):
    #     qs = self
    #     final_array = []
    #     for obj in qs:
    #         struct = json.loads(obj.serialize())
    #         final_array.append(struct)
    #     return json.dumps(final_array)

    # more efficient way to serialize data
    def serialize(self):
        list_values = list(self.values("user", "content", "image"))
        print(list_values)
        return json.dumps(list_values)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    # inefficient
    # def serialize(self):
    #     json_data = serialize("json", [self], fields=("user", "content", "image"))
    #     struct = json.loads(json_data)  # list of a dict -> [{}]
    #     print(struct)
    #     data = json.dumps(struct[0]["fields"])
    #     return data

    def serialize(self):
        image = self.image
        if image:
            image = self.image.url
        else:
            image = ""
        data = {
            "id": self.id,
            "content": self.content,
            "user": self.user.id,
            "image": image,
        }
        data = json.dumps(data)
        return data
