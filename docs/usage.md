# Usage

1. We start by adding urlpattern
```python
from django.urls import path, include

urlpatterns = [
    ...,
    path('api/2fa/', include("drf_2fa.urls")),
    ...,
]
```

