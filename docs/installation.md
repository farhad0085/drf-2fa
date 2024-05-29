# Installation

Ensure a secure authentication layer in your Django project by following these simple steps:

1. Install the package
```sh
pip install drf_2fa
```

2. Add `drf_2fa` to your `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'drf_2fa',
    ...
]
```

3. Configure DRF 2FA by referring to the [Configuration Guide](./configuration.md)

4. Apply database migrations:
```sh
python manage.py migrate
```

5. Learn how to use DRF 2FA effectively in the [Usage Guide](./usage.md)