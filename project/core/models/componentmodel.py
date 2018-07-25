# -*- coding: utf-8 -*-
from django.db import models

class Component(models.Model):
    component_type = models.ForeignKey('core.ComponentType', on_delete=models.CASCADE)

    connection_type = models.ForeignKey('core.ConnectionType', on_delete=models.CASCADE)

    type = models.CharField( max_length=45 )
    outside_shape = models.CharField( max_length=45 )

    base_type = models.CharField( max_length=45 )

    height_over_tube = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)

    bolt_pattern_long = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)	
    bolt_pattern_wide = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)	
    groove = models.BooleanField( default = False)
    base_diameter = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)	
    shoulder_diameter = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)	
    unique_feature = models.BooleanField( default = False)
    orientation = models.BooleanField( default = False)	
    weight = models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)	
