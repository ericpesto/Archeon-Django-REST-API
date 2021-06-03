from rest_framework import serializers
from ..models import StockLink

class StockLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockLink
        fields = '__all__'