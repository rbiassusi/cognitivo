# -*- coding: utf-8 -*-
from django.db import models

class TubeAssembly(models.Model):
	components = models.ManyToManyField('core.Component', through = 'AssemblyComponent' )


class AssemblyComponent(models.Model):
	tube_assembly = models.ForeignKey( 'TubeAssembly', on_delete=models.CASCADE )
	component = models.ForeignKey( 'core.Component', on_delete=models.CASCADE )
	quantity = models.IntegerField()
	