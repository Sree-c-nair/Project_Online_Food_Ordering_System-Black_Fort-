from django.urls import path
from . import views
from .views import MenuSearch, FoodDetails, OrderConfirmation

urlpatterns = [
    path('', views.Home, name='home'),
    path('contact', views.Contact, name='contact'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    path('register/', views.signup, name='register'),
    path('food/', views.food, name='food'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_order'),
    path('menu/search/', MenuSearch.as_view(), name='menu-search'),
    path('view-food/<int:pk>', FoodDetails.as_view(), name='view-food'),
    path('order-confirmation/', OrderConfirmation.as_view(), name='order-confirmation'),

]
