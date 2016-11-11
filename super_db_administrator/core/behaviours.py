
from django.db import models

from core.utils import unique_slugify


class SlugableBehaviour(models.Model):

    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, **kwargs):
        slug_str = "{}".format(self.name)
        unique_slugify(self, slug_str)
        super(SlugableBehaviour, self).save(**kwargs)

    class Meta:
        abstract = True
