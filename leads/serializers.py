from rest_framework import serializers
from .models import Lead

class LeadSerializer(serializers.ModelSerializer):
    class meta:
        model = Lead
        fields = ('id', 'name', 'email', 'message')