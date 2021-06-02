from time import sleep
from celery import shared_task
from .models import StockDetails
from nsetools import Nse

nse = Nse()


@shared_task
# some heavy stuff here
def update_data():
    print('Updating stock data ..')
    stock_list = StockDetails.objects.all()
    for stock_item in stock_list:
        current_stock_data = nse.get_quote(stock_item.stock_code)
        # create dictionary
        updated_data = {
            'stock_name': current_stock_data['companyName'],
            'stock_code': current_stock_data['symbol'],
            'current_price': current_stock_data['lastPrice'],
            'average_price': current_stock_data['averagePrice'],
            'opening_price': current_stock_data['open'],
            'closing_price': current_stock_data['closePrice'],
            'previous_closing_price': current_stock_data['previousClose'],
            'percent_change': current_stock_data['pChange'],
            'absolute_change': current_stock_data['change'],
            'day_high_price': current_stock_data['dayHigh'],
            'day_low_price': current_stock_data['dayLow'],
            'high_52week_price': current_stock_data['high52'],
            'low_52week_price': current_stock_data['low52'],
            'face_value': current_stock_data['faceValue'],
            'total_traded_volume': current_stock_data['totalTradedVolume'],
            'upper_circuit_price': current_stock_data['pricebandupper'],
            'lower_circuit_price': current_stock_data['pricebandlower'],
            'delivery_to_traded_quantity': current_stock_data['deliveryToTradedQuantity']
        }
        # find the object by filtering and update all fields
        StockDetails.objects.filter(
            stock_code=current_stock_data['symbol']).update(**updated_data)
        sleep(5)


while True:
    # updating data every 120 seconds
    sleep(120)
    update_data()
