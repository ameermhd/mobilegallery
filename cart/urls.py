from django.urls import path
from .import views

urlpatterns = [

    path('cart_item',views.cart_Details,name='cartdet'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='min'),
    path('del/<int:product_id>/', views.cart_delete, name='del'),

]