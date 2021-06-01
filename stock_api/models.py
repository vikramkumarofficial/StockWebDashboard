from django.db import models

# Create your models here.


class StockCodes(models.Model):
    stock_name = models.CharField(
        max_length=255, default="", null=False, db_index=True)
    stock_code = models.CharField(
        max_length=255, default="", null=False, db_index=True)
