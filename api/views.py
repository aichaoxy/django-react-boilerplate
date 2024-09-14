from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from datetime import datetime

@api_view(['GET'])
def index(request):
    current_time = datetime.now().strftime("%-I:%S %p")
    current_date = datetime.now().strftime("%d/%m/%-Y")
    data = {
        'time': current_time,
        'date': current_date
    }
    return Response(data)

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

class TodoView(viewsets.ModelViewSet):

    # create a serializer class and 
    # assign it to the TodoSerializer class
    serializer_class = TodoSerializer

    # define a variable and populate it 
    # with the Todo list objects
    queryset = Todo.objects.all()