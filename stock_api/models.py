from django.db import models

# Create your models here.


class StockCodes(models.Model):
    stock_name = models.CharField(
        max_length=255, default="", null=False, db_index=True)
    stock_code = models.CharField(
        max_length=255, default="", null=False, db_index=True)


class StockDetails(models.Model):
    stock_name = models.CharField(
        max_length=255, default="", null=False, db_index=True)
    stock_code = models.CharField(
        max_length=255, default="", null=False, db_index=True)
    current_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    average_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    opening_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    closing_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    previous_closing_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    percent_change = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    absolute_change = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    day_high_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    day_low_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    high_52week_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    low_52week_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    face_value = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    total_traded_volume = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    upper_circuit_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    lower_circuit_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)
    delivery_to_traded_quantity = models.DecimalField(
        max_digits=10, decimal_places=2, null=True)


class MarketWatchList(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(
        max_length=255, default="", null=False, db_index=True)
    stock_list = models.ManyToManyField(
        StockDetails, related_name='stock_list', blank=True)
