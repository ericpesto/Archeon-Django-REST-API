from rest_framework import serializers
from ..models import StockActivity

class StockActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = StockActivity
        fields = '__all__'