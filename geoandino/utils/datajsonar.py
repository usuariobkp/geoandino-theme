# -*- coding: utf-8 -*-
from django.conf import settings
from geoandino.utils.conf import get_site_conf

def data_jsonar():
    site_conf = get_site_conf()
    """Return data.json(ar) representation of catalogue"""

    return {
        "title": site_conf.title,
        "description": site_conf.description,
        "publisher": {
            "name": site_conf.publisher.user.username,
            "mbox": site_conf.publisher.email,
        },
        "superThemeTaxonomy": settings.SUPER_THEME_TAXONOMY_URL,
        "datasets": [],
    }