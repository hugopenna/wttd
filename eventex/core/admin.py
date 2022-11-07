from django.contrib import admin
from django.utils.html import format_html

from eventex.core.models import Speakers, Contacts, Talk


class ContactInline(admin.TabularInline):
    model = Contacts
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return format_html('<a href="{0}">{0}</a>', obj.website)

    website_link.short_description = 'website'

    def photo_img(self, obj):
        return format_html('<img width="32px" src="{}" />', obj.photo)

    photo_img.short_description = 'foto'

    def email(self, obj):
        return Contacts.emails.filter(speaker=obj).first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return Contacts.phones.filter(speaker=obj).first()

    phone.short_description = 'telefone'

admin.site.register(Speakers, SpeakerModelAdmin)
admin.site.register(Talk)