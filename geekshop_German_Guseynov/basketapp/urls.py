from django.urls import path
import basketapp.views as basketapp

app_name = 'basket'

urlpatterns = [
    path('', basketapp.basket, name='view'),
    path('add/<int:pk>', basketapp.add, name='add'),
    # path('delete/<int:pk>', basketapp.delete, name='delete'),
    path('remove/ajax/<int:pk>/', basketapp.basket_remove_ajax, name='remove'),
    path('edit/<int:pk>/<int:quantity>/', basketapp.basket_edit, name='edit')
]