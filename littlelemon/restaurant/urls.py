#define URL route for index() view
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from . import views
from .views import *

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.MenuItemView.as_view(), name='menu'),
    path('reservations/', views.reservations, name="reservations"),
    # API paths
    path('menu/<int:pk>', views.SingleItemMenuView.as_view(), name='menu-item'),
    path('booking/', include(router.urls)),
]
