from rest_framework import serializers
from .models import points

class pointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = points
        fields = '__all__'
