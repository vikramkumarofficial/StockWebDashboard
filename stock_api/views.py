from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from nsetools import Nse
from stock_api.models import StockCodes, MarketWatchList, StockDetails
from stock_api.serializers import StockCodesSerializer, StockDetailsSerializer, MarketWatchListSerializer
# Create your views here.


class StockCodesView(APIView):

    def get(self, request):
        try:
            nse = Nse()
            stock_list = nse.get_stock_codes(cached=False)
            # StockCodes.objects.all().delete()
            for key, value in stock_list.items():
                stock_code_obj = StockCodes(stock_name=value, stock_code=key)
                stock_code_obj.save()
            snippets = StockCodes.objects.all()
            serializer = StockCodesSerializer(snippets, many=True)
            response = Response(serializer.data)
            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SearchStockCodesView(APIView):

    def get(self, request, searchTerm):
        try:
            if (searchTerm is not None) and (len(str(searchTerm).strip()) != 0):
                snippets = StockCodes.objects.filter(
                    stock_name__contains=searchTerm)
                serializer = StockCodesSerializer(snippets, many=True)
                response = Response(serializer.data)
                return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class AddMarketWatchListView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            stock_code = request.data.get('stock_code')
            stock_name = request.data.get('stock_name')
            if username is None:
                return Response({'error': 'Invalid User Name'})
            elif stock_name is None:
                return Response({'error': 'Invalid Stock Name'})
            elif stock_code is None:
                return Response({'error': 'Invalid Stock Code'})
            else:
                if MarketWatchList.objects.filter(user_name=username).exists():
                    stock_details = StockDetails(
                        stock_name=stock_name, stock_code=stock_code)
                    stock_details.save()
                    market_watch_list = MarketWatchList.objects.filter(
                        user_name=username).first()
                    market_watch_list.stock_list.add(stock_details)
                    market_watch_list.save()
                else:
                    stock_details = StockDetails(
                        stock_name=stock_name, stock_code=stock_code)
                    market_watch_list = MarketWatchList(
                        user_name=username)
                    stock_details.save()
                    market_watch_list.save()
                    market_watch_list.stock_list.add(stock_details)
                    market_watch_list.save()
                data = MarketWatchList.objects.filter(user_name=username)
                serializer = MarketWatchListSerializer(data, many=True)
                return Response(data=serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
