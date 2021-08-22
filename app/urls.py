from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('<slug:c_slug>/',views.home,name='pro_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodet,name='pro_det'),
    path('serch',views.serch,name='serch'),

]