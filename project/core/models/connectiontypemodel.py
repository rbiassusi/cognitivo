# -*- coding: utf-8 -*-
from django.db import models

class ConnectionType(models.Model):
	name = models.CharField( max_length=45 )