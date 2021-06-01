from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from nsetools import Nse
from stock_api.models import StockCodes
from stock_api.serializers import StockCodesSerializer
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
