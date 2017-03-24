from django.contrib.postgres.fields import JSONField
from django.db import models


class Crash(models.Model):
    created = models.DateTimeField('Created Time', null=False, auto_now_add=True)
    device_id = models.CharField('Device ID', max_length=100, null=True, blank=True)
    error = JSONField('Error', null=False, )

    class Meta:
        db_table = 'crash'
        verbose_name = "Crash"
        verbose_name_plural = "Crashes"
        app_label = 'crash'
