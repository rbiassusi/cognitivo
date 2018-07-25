# -*- coding: utf-8 -*-
from django.db import models

class PriceQuote(models.Model):
    tube_assembly = models.ForeignKey('core.TubeAssembly', on_delete=models.CASCADE)
    supplier = models.ForeignKey('core.Supplier', on_delete=models.CASCADE)
    quote_date = models.DateField()
    annual_usage = models.IntegerField( default = 0)
    min_order_quantity = models.IntegerField( default = 0 )
    bracket_pricing = models.BooleanField(default = True)
    quantity = models.IntegerField()
    cost = models.DecimalField(blank=True, decimal_places=5, default=0, max_digits=19, null=True)