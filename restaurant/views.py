from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from .models import Menu, Book
from .serializers import menuSerializer, bookSerializer, UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, renderer_classes, permission_classes, throttle_classes
 

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class bookingview(APIView):
    def get(self, request):
        items = Book.objects.all()
        serializer = bookSerializer(items, many=True)
        return Response(serializer.data)
    
class menuview(APIView):
    def post(self, request):
        serializer = menuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    #search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

    def get_permissions(self):
        permission_classes = []
        if self.request.method != 'GET':
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 