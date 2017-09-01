# -*- coding: utf-8 -*-

from geoandino.models import SiteConfiguration
from django.contrib.staticfiles.templatetags.staticfiles import static


class NullSiteConfiguration:
    def __init__(self):
        self.title = "Título del Portal"
        self.description = "<b>Describí el portal.</b> Explicá de qué se trata tu catálogo de datos geoespaciales. " \
                           "Por favor, hacelo en no más de tres líneas."
        self.layer_description = "Estos son los conjuntos de datos espaciales y vectoriales disponibles."
        self.document_description = ""
        self.map_description = ""
        self.image_background_url = static('img/bg-jumbotron.jpg')
        self.logo_header_url = static('img/logo_ministerio.svg')
        self.logo_footer_url = static('img/argentinagob.svg')
        self.about_visible = True
        self.group_visible = True
        self.default = True
    

def get_nullobject_site_conf():
    return NullSiteConfiguration()


def get_site_conf():
    query = SiteConfiguration.objects.filter(default=True)
    if query.exists():
        return query.first()
    else:
        return get_nullobject_site_conf()
