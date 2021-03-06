# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django import forms
from announcements import forms as announcements_forms
from account import forms as account_forms
from geonode.groups import forms as group_forms
from geonode.groups.models import GroupProfile
from slugify import slugify


class AnnouncementI18nForm(announcements_forms.AnnouncementForm):
    """
    Override original announcements's form for adding translations
    """

    class Meta(announcements_forms.AnnouncementForm.Meta):
        labels = {
            'title': _('title'),
            'level': _('level'),
            'content': _('content'),
            'site_wide': _('site wide'),
            'members_only': _('members only'),
            'desmissal_type': _('dissmissal type'),
            'publish_start': _('publish start'),
            'publish_end': _('publish end'),
        }


class SignupCodeI18nForm(account_forms.SignupCodeForm):
    username = forms.CharField(max_length=30, required=False, label=_("Username"))


def group_titles():
    groups = GroupProfile.objects.all()
    return list(map(lambda g: g.title, groups))


def group_choices():
    choices = [('default', _("It doesn't depend on another group"))]
    for title in group_titles():
        choices.append((title, title))
    return choices


def add_dependency_field(form):
    form.base_fields['depends_on_group'] = forms.ChoiceField(label=_('Does it depend on another group?'),
                                                             choices=group_choices(),
                                                             widget=forms.Select())


def clean_update_form(self):
    cleaned_data = self.cleaned_data

    name = cleaned_data.get("title")
    if name is None:
        raise forms.ValidationError(
            _("You should write a name for the group."))
    slug = slugify(name)

    cleaned_data["slug"] = slug

    return cleaned_data


add_dependency_field(group_forms.GroupForm)
add_dependency_field(group_forms.GroupUpdateForm)
group_forms.GroupForm.clean = clean_update_form

