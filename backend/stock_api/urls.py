from django.urls import path
from stock_api.views import StockCodesView, SearchStockCodesView, AddMarketWatchListView

urlpatterns = [
    path('getAllStocks/', StockCodesView.as_view(), name='get_all_stocks'),
    path('searchStocks/<str:searchTerm>',
         SearchStockCodesView.as_view(), name='search_stocks'),
    path('marketWatchList/',
         AddMarketWatchListView.as_view(), name='market_watchlist')
]
