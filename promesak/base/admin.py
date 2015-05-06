from django.contrib import admin
from promesak.base.models import Party
from promesak.base.models import Promise
from tinymce.widgets import TinyMCE
from django.forms import ModelForm
from django.conf import settings


# Register your models here.
class PartyAdmin(admin.ModelAdmin):
    pass


class PromiseForm(ModelForm):

    class Meta:
        model = Promise
        fields = ['slug', 'title', 'text', 'date_promised',
            'source_promise_url', 'source_promise_text',
            'party', 'fulfilled', 'fulfillment_proof', 'date_fulfilled']
        widgets = {
            'text': TinyMCE(attrs={'cols': 100, 'rows': 15}),
            'source_promise_text': TinyMCE(attrs={'cols': 100, 'rows': 15}),
            'fulfillment_proof': TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }


class PromiseAdmin(admin.ModelAdmin):

    form = PromiseForm

    list_display = ('title', 'party', 'date_promised',)
    list_filter = ('party',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('text', 'source_promise_text', 'fulfillment_proof'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs=settings.TINYMCE_BODY_CONFIG,
            ))

        return super(PromiseAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Party, PartyAdmin)
admin.site.register(Promise, PromiseAdmin)
