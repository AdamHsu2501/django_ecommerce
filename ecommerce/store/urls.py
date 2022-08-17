from django.urls import path
from .views import store, cart, checkout, updateItem, processOrder

urlpatterns = [
    path('', view=store, name='store'),
    path('cart/', view=cart, name='cart'),
    path('checkout/', view=checkout, name='checkout'),

    path('update_item/', view=updateItem, name='update_item'),
    path('process_order/', view=processOrder, name='process_order'),
]
