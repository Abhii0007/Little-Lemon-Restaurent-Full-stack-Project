from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import MenuItem, Cart, Order
from .serializers import MenuItemSerializer, CartSerializer, OrderSerializer, RegisterUserSerializer
from django.contrib.auth.models import User

# User Registration View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


class UserRegistrationView(APIView):
    permission_classes = []  # No authentication required

    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CustomLoginView(APIView):
    authentication_classes = []  # 🚫 Disable default authentication
    permission_classes = [permissions.AllowAny]  # ✅ Allow any user

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)






from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


class AddUserToManagerGroupView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated with a token
    authentication_classes = [TokenAuthentication]  # Use token-based authentication
    
    def post(self, request):
        username = request.data.get('username')
        
        if not username:
            return Response({"detail": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Fetch the user
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise NotFound(detail="User not found.")
        
        # Fetch the "manager" group
        manager_group, created = Group.objects.get_or_create(name='manager')

        # Add user to the "manager" group
        user.groups.add(manager_group)

        return Response({"detail": f"User {username} added to manager group."}, status=status.HTTP_200_OK)












# MenuItem Views
from rest_framework.permissions import AllowAny

class MenuItemListCreateView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    #permission_classes = [IsAdminUser]  # Only admin can access this view

class MenuItemRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [AllowAny]  # Only admin can access this view


# Cart Views
from rest_framework.permissions import IsAuthenticated

class CartListCreateView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# Order Views
from rest_framework.permissions import IsAuthenticated

from .permissions import IsManager

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsManager]  # Only 'Manager' group members can access this view

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this

