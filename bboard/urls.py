from django.urls import path
from .views import index
from .views import promo


urlpatterns = [
    path('', index, name="index"),
    path("1", promo, name="promo")
]