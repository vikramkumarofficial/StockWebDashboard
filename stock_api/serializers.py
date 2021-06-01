from rest_framework import serializers
from stock_api.models import StockCodes


class StockCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCodes
        fields = '__all__'
