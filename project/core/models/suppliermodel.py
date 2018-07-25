# -*- coding: utf-8 -*-
from django.db import models

class Supplier(models.Model):
	name = models.CharField( max_length=45, blank = True, null = True )