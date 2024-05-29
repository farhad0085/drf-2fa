# Installation

1. Install the package
```sh
pip install drf_2fa
```

2. Add `drf_2fa` to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    ...
    'drf_2fa',
    ...
]
```

3. [Configuration](./configuration.md)

4. Migrate database changes:
```
python manage.py migrate
```

5. [Usage](./usage.md)