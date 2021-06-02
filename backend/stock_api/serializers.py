from rest_framework import serializers
from stock_api.models import StockCodes, StockDetails, MarketWatchList


class StockCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockCodes
        fields = '__all__'


class StockDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockDetails
        fields = '__all__'


class MarketWatchListSerializer(serializers.ModelSerializer):
    stock_list = StockDetailsSerializer(many=True, read_only=True)

    class Meta:
        model = MarketWatchList
        fields = ("user_name", "stock_list")
