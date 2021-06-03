from rest_framework import serializers
from ..models import ActivityDefinition

class ActivityDefinitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityDefinition
        fields = '__all__'
