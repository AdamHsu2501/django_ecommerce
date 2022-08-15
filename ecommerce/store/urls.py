from django.urls import path
from .views import store, cart, checkout

urlpatterns = [
    path('', view=store, name='store'),
    path('cart/', view=cart, name='cart'),
    path('checkout/', view=checkout, name='checkout')
]
