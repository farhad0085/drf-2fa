"""
Inspired by `djangorestframework` settings
"""

from django.conf import settings
from django.test.signals import setting_changed
from django.utils.module_loading import import_string
import datetime


DEFAULT_SETTINGS = {
    "DEFAULT_OTP_BACKEND": "drf_2fa.backends.email.EmailOTPBackend",
    "OTP_LENGTH": 6,
    "OTP_EXPIRE": datetime.timedelta(seconds=86400),
    "OTP_EMAIL_FROM": settings.DEFAULT_FROM_EMAIL,
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = [
    'DEFAULT_OTP_BACKEND',
]

def perform_import(val, setting_name):
    """
    If the given setting is a string import notation,
    then perform the necessary import or imports.
    """
    if val is None:
        return None
    elif isinstance(val, str):
        return import_from_string(val, setting_name)
    elif isinstance(val, (list, tuple)):
        return [import_from_string(item, setting_name) for item in val]
    return val


def import_from_string(val, setting_name):
    """
    Attempt to import a class from a string representation.
    """
    try:
        return import_string(val)
    except ImportError as e:
        msg = "Could not import '%s' for API setting '%s'. %s: %s." % (val, setting_name, e.__class__.__name__, e)
        raise ImportError(msg)



class Settings:
    """
    A settings object that allows drf_2fa settings to be accessed as
    properties. For example:

        from drf_2fa.settings import drf_2fa_settings
        print(drf_2fa_settings.DEFAULT_OTP_BACKEND)

    Any setting with string import paths will be automatically resolved
    and return the class, rather than the string literal.

    Note:
    This is an internal class that is only compatible with settings namespaced
    under the DRF_2FA_SETTINGS name. It is not intended to be used by 3rd-party
    apps, and test helpers like `override_settings` may not work as expected.
    """
    def __init__(self, defaults=None, import_strings=None):
        self.defaults = defaults or DEFAULT_SETTINGS
        self.import_strings = import_strings or IMPORT_STRINGS
        self._cached_attrs = set()

    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'DRF_2FA_SETTINGS', {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError("Invalid API setting: '%s'" % attr)

        try:
            # Check if present in user settings
            val = self.user_settings[attr]
        except KeyError:
            # Fall back to defaults
            val = self.defaults[attr]

        # Coerce import strings into classes
        if attr in self.import_strings:
            val = perform_import(val, attr)

        # Cache the result
        self._cached_attrs.add(attr)
        setattr(self, attr, val)
        return val

    def reload(self):
        for attr in self._cached_attrs:
            delattr(self, attr)
        self._cached_attrs.clear()
        if hasattr(self, '_user_settings'):
            delattr(self, '_user_settings')


drf_2fa_settings = Settings(DEFAULT_SETTINGS, IMPORT_STRINGS)


def reload_drf_2fa_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == 'DRF_2FA_SETTINGS':
        drf_2fa_settings.reload()


setting_changed.connect(reload_drf_2fa_settings)
