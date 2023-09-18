from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleItemMenuView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    
class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html')

def reservations(request:HttpRequest) -> HttpResponse:
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'reservations.html',{"bookings":booking_json})