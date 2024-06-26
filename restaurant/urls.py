#define URL route for index() view
from django.urls import path
from . import views
from .views import menuview, bookingview
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    #path('menu/', menuview.as_view()),
    #path('booking/', bookingview.as_view()),
    path('booking/', views.BookView.as_view()),
    path('booking/<int:pk>', views.SingleBookView.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),

]
