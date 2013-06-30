from django.db import models

from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Photo(models.Model):
    class Meta:
        verbose_name = _('Photo')
        verbose_name_plural = _('Photos')

    def __self__(self):
        return self.pk

    image = models.ImageField(upload_to = 'photos', blank = True, null = True)