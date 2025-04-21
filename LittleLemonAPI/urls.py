from django.urls import path
from .views import UserRegistrationView,CustomLoginView,MenuItemListCreateView, MenuItemRetrieveUpdateDeleteView, CartListCreateView, OrderListCreateView, OrderDetailView,AddUserToManagerGroupView

urlpatterns = [
    path('api/users', UserRegistrationView.as_view(), name='user-register'),
    path('api/menu-items', MenuItemListCreateView.as_view(), name='menu-items-list'),
    path('api/menu-items/<int:pk>', MenuItemRetrieveUpdateDeleteView.as_view(), name='menu-items-detail'),
    path('api/cart/menu-items', CartListCreateView.as_view(), name='cart-list'),
    path('api/orders', OrderListCreateView.as_view(), name='orders-list'),
    path('api/orders/<int:pk>', OrderDetailView.as_view(), name='order-detail'),
    
    path('api/auth/token', CustomLoginView.as_view(), name='user-auth'),
    path('groups/manager/users', AddUserToManagerGroupView.as_view(), name='add-user-to-manager-group'),


    
]
