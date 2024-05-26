# For admin panel customization
JAZZMIN_SETTINGS = {
    "copyright": "DRF 2FA",
    "search_model": ["user.UserAccount"],
    "topmenu_links": [
        {"name": "Home",  "url": "/"},
    ],
    "related_modal_active": True,
    "show_ui_builder": True,
    "order_with_respect_to": [
        "user", "user.UserAccount"
    ],

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": ['authtoken', 'auth'],

    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "DRF 2FA",
    # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "DRF 2FA",
    # Title on the brand (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_brand": "DRF 2FA",
}
