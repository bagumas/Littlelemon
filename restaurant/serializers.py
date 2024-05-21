from rest_framework import serializers
from .models import Book, Menu
from django.contrib.auth.models import User


class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['url', 'username', 'email', 'groups']
        fields = ['username', 'email', 'id','first_name','last_name']