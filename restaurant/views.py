from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissions
from .models import Menu, Book
from .serializers import menuSerializer, bookSerializer, UserSerializer
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view, renderer_classes, permission_classes, throttle_classes
from rest_framework.authtoken.models import Token

#token = Token.objects.create(user=request.user)
#print(token.key)

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
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
    #search_fields = ['category__title']
    ordering_fields = ['price', 'inventory']

 


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

 

#@permission_classes([IsAuthenticated])
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = bookSerializer


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [IsAuthenticated] 


@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message":"This view is protected"})