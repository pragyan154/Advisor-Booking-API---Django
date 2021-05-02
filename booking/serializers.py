from .models import Advisor ,booking
from rest_framework.serializers import ModelSerializer

class AdvisorSerializers(ModelSerializer):

    class Meta:
        model= Advisor
        fields = ['id','advisor_name','advisor_photoURL']

class BookingSerializers(ModelSerializer):
    class Meta:
        model = booking
        fields = ['id','datetime','userid','advisorid']