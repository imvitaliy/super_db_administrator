from django.contrib.postgres.fields import JSONField
from django.db import models

from core.behaviours import SlugableBehaviour

class EntityType(SlugableBehaviour, models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tipo de Entidad"
        verbose_name_plural = "Tipos de Entidades"

class Entity(SlugableBehaviour, models.Model):

    name = models.CharField(max_length=255)
    parent_entity = models.ForeignKey("self", blank=True, null=True, related_name='child_entities')
    entity_type = models.ForeignKey(EntityType, related_name='entities', blank=True, null=True)
    standart_info = JSONField(blank=True, null=True, default={})
    scraper_info = JSONField(blank=True, null=True, default={})
    page_content = JSONField(blank=True, null=True, default={})

    def __str__(self):
        return '{} - {}'.format(self.name, self.entity_type.name)

    class Meta:
        verbose_name = "Entidad Local"
        verbose_name_plural = "Entidades Locales"
