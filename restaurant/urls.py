from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookingViewSet, MenuViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'menu', MenuViewSet)

urlpatterns = [
    
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('bookings/', views.bookings, name="bookings"),
    path('api/', include(router.urls)),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')), 
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
