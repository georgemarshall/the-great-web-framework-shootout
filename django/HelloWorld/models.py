from django.db import models
from django.utils.translation import ugettext_lazy as _


class Hello(models.Model):
    data = models.CharField(_('data'), max_length=255)

    class Meta:
        db_table = 'hello'

    def __unicode__(self):
        return u'%s, %s' % (self.id, self.data)
