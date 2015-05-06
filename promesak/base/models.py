from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify


class Party(models.Model):
    slug = models.SlugField(
        'Slug', max_length=255, unique=True, blank=True, null=True)
    name = models.CharField(_('Title'), max_length=255)
    text = models.TextField(_('Text'), default=u'')
    candidates = models.TextField(_('Candidates'), default=u'')
    web = models.CharField(_('Web'), max_length=255, default=u'',)
    logo = models.ImageField(_('Logo'),
        upload_to='uploads', blank=True, null=True)
    program_file = models.FileField(_('Program file'),
        upload_to='uploads', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            slug = slugify(self.name)[:200]
            while Party.objects.filter(slug=slug):
                slug = slug + '-1'
            self.slug = slug
        super(Party, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Promise(models.Model):
    slug = models.SlugField(
        'Slug', max_length=255, unique=True, blank=True, null=True)
    title = models.CharField(_('Title'), max_length=255)
    text = models.TextField(_('Text'), default=u'')
    date_promised = models.DateField(_('Promise date'), blank=True, null=True)
    source_promise_url = models.CharField(_('Source URL'), max_length=255)
    source_promise_text = models.TextField(
        _('Extra promise text'), default=u'')
    party = models.ForeignKey(Party, blank=True, null=True)

    fulfilled = models.BooleanField(
        _('Fulfilled?'), default=False)
    fulfillment_proof = models.TextField(
        _('Fulfillment proof'), default=u'', blank=True, null=True)
    date_fulfilled = models.DateField('Date fulfilled', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            slug = slugify(self.title)[:200]
            while Promise.objects.filter(slug=slug):
                slug = slug + '-1'
            self.slug = slug
        super(Promise, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title
