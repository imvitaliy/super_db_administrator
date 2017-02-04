from django.db import models

from core.behaviours import SlugableBehaviour


class ConnectionDb(SlugableBehaviour, models.Model):
    name = models.CharField(max_length=100, default="")
    db_name = models.CharField(max_length=200, blank=False, null=False)
    host = models.CharField(max_length=500, blank=False, null=False)
    port = models.IntegerField(blank=False, null=False)
    ssl = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=200, blank=False, null=False)
    password = models.CharField(max_length=200, blank=False, null=False)


    def create(self, data):
            """
            Create and return a new `Snippet` instance, given the validated data.
            """
            return self.objects.create(**data)
