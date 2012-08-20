# -*- coding: utf-8 -*-

from django.utils.encoding import force_unicode
from django.utils.functional import wraps
from django.template.defaultfilters import lower
from django.conf import settings

def parse_tags(tagstring):
    """
    Parses tag input, with multiple word input being activated and
    delineated by commas and double quotes. Quotes take precedence, so
    they may contain commas.

    Returns a sorted list of unique tag names.

    Ported from Jonathan Buchanan's `django-tagging
    <http://django-tagging.googlecode.com/>`_
    """
    if not tagstring:
        return []

    # Should all tags be handled as lowercase?
    try:
        settings.TAGGIT_FORCE_LOWERCASE
        tagstring = lower(force_unicode(tagstring))
    except:
        tagstring = force_unicode(tagstring)

    tagstring = tagstring.replace(u'，', ', ')
    words = split_strip(tagstring)

    return words


def split_strip(string, delimiter=u','):
    """
    Splits ``string`` on ``delimiter``, stripping each resulting string
    and returning a list of non-empty strings.

    Ported from Jonathan Buchanan's `django-tagging
    <http://django-tagging.googlecode.com/>`_
    """
    if not string:
        return []

    words = [w.strip() for w in string.split(delimiter)]
    return [w for w in words if w]


def edit_string_for_tags(tags):
    names = [tag.name for tag in tags]
    return u', '.join(names)


def require_instance_manager(func):
    @wraps(func)
    def inner(self, *args, **kwargs):
        if self.instance is None:
            raise TypeError("Can't call %s with a non-instance manager" % func.__name__)
        return func(self, *args, **kwargs)
    return inner
