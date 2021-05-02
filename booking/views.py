from django.shortcuts import render
from rest_framework.generics import CreateAPIView , ListAPIView , ListCreateAPIView
from rest_framework.views import APIView
from .models import Advisor, booking
from .serializers import AdvisorSerializers , BookingSerializers
from rest_framework import permissions
from authentication.views import LoginView
from rest_framework.response import Response
from django.contrib.auth.models import User

class AddAdvisor(CreateAPIView):
    serializer_class = AdvisorSerializers
    def perform_create(self, serializer):
        serializer.save()

class getAdvisor(ListAPIView):
    serializer_class = AdvisorSerializers
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Advisor.objects.all()


class addbooking(ListCreateAPIView):
    serializer_class = BookingSerializers 
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request,pk,key):
        userid = pk
        advisorid = key
        data = request.data
        result = booking.objects.filter(userid=userid,advisorid=advisorid).count()
        print(result)
        if Advisor.objects.filter(id=advisorid).exists() and User.objects.filter(id=userid).exists() == True and result < 1:
            new_booking = booking.objects.create(datetime=data["datetime"] ,userid=userid,advisorid=advisorid)

            new_booking.save()
            serializer = BookingSerializers(new_booking)
            return Response(serializer.data)
        else:
            res = {'error': 'User or Advisor does not exist '}
            return Response(res)
class BookDetail(ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = BookingSerializers
    
    def get(self,request,pk):
        userid = pk

        data= booking.objects.get(userid=userid)
        serializer = BookingSerializers(data)
        advisorid = serializer.data['advisorid']

        data2 = Advisor.objects.get(id=advisorid)
        serializer2 = AdvisorSerializers(data2)

        finaldata = (serializer2.data,serializer.data)
        return Response(finaldata)
