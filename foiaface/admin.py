from django.contrib import admin
from foiaface.models import Jurisdiction, Contact, Request

class JurisdictionAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'parent_jurisdiction', 'jurisdiction_type')
    list_filter = ('jurisdiction_type',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')

class RequestAdmin(admin.ModelAdmin):
    pass

admin.site.register(Jurisdiction, JurisdictionAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Request, RequestAdmin)
