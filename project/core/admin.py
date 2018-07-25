from django.contrib import admin
from .models import *


@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    pass

@admin.register(ConnectionType)
class ConnectionTypeAdmin(admin.ModelAdmin):
    pass    

@admin.register(ComponentType)
class ComponentTypeAdmin(admin.ModelAdmin):
    pass  

class ComponentInlineAdmin(admin.TabularInline):
	model = AssemblyComponent

@admin.register(TubeAssembly)
class TubeAssemblyAdmin(admin.ModelAdmin):
    inlines = [ComponentInlineAdmin, ]

@admin.register(PriceQuote)
class PriceQuoteAdmin(admin.ModelAdmin):
    pass  

