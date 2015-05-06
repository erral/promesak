from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from django.conf import settings


class PageForm(FlatpageForm):

    class Meta:
        model = FlatPage
        widgets = {
            'content': TinyMCE(attrs={'cols': 100, 'rows': 15}),
        }


class PageAdmin(FlatPageAdmin):
    """
    Page Admin
    """
    form = PageForm

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('content', ):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs=settings.TINYMCE_BODY_CONFIG,
            ))

        return super(PageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
