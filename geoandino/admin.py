# -*- coding: utf-8 -*-
from django.contrib import admin
from geoandino.models import SiteConfiguration, FacebookAndGoogleMetadata, TwitterMetadata
from django.utils.translation import ugettext as _


class FacebookAndGoogleMetadataInline(admin.StackedInline):
    model = FacebookAndGoogleMetadata
    max_num = 1
    verbose_name_plural = _('Social Media Metadata')
    verbose_name = _('Facebook and Google')
    fields = ['title', 'description', 'image']


class TwitterMetadataInline(admin.StackedInline):
    model = TwitterMetadata
    max_num = 1
    verbose_name_plural = _('Social Media Metadata')
    verbose_name = _('Twitter')
    fields = ['title', 'description', 'image']


class SiteConfigurationAdmin(admin.ModelAdmin):
    list_display = ('title', 'default')
    fieldsets = [
        (None, {'fields': [_('default')]}),
        (_('Landing'), {'fields': [_('title'), _('description'), _('image_background')]}),
        (_('Layers, documents and maps'), {'fields': [_('layer_description'), _('document_description'), _('map_description')]}),
        (_('Contact'), {'fields': [_('facebook_url'), _('twitter_url'), _('github_url'), _('instagram_url'), _('youtube_url'), _('contact_mail')]}),
        (_('About (optional)'), {'fields': [_('about_title'), _('about_description'), _('about_visible')]}),
    ]

    inlines = [FacebookAndGoogleMetadataInline, TwitterMetadataInline]

admin.site.register(SiteConfiguration, SiteConfigurationAdmin)
