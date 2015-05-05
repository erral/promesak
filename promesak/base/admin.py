from django.contrib import admin
from promesak.base.models import Party
from promesak.base.models import Promise


# Register your models here.
class PartyAdmin(admin.ModelAdmin):
    pass


class PromiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'party', 'date_promised',)
    list_filter = ('party',)


admin.site.register(Party, PartyAdmin)
admin.site.register(Promise, PromiseAdmin)
