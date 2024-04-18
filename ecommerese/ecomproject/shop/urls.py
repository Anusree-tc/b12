from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('<slug:slug_c>/',views.home,name="product_by_category"),
    path('base/',views.base,name='base'),



]