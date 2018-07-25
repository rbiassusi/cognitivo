# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

from core.models import *

import csv

class Command(BaseCommand):
    def handle(self, **options):
        importComponent()
        importBillOfMaterials()
        importPriceQuote()

def importComponent():
    reader = csv.DictReader(open('../data/comp_boss.csv'))

    arr_components = []
    for row in reader:
        component_id = int(row['component_id'].replace('C-',''))
        component_type_id = int(row['component_type_id'].replace('CP-',''))
        connection_type_id = int(row['connection_type_id'].replace('B-',''))



        component_type, created = ComponentType.objects.get_or_create(pk=component_type_id, name=row['component_type_id'])
        connection_type, created = ConnectionType.objects.get_or_create(pk=connection_type_id, name=row['connection_type_id'])

        del row['component_id']
        del row['component_type_id']
        del row['connection_type_id']

        new_component_dict = {k:v for k,v in row.items() if v != 'NA'}
        new_component_dict.update({k:False for k,v in row.items() if v == 'No' })
        new_component_dict.update({k:True for k,v in row.items() if v == 'Yes' })
        new_component_dict.update({'pk': component_id, 'component_type': component_type, 'connection_type': connection_type})

        new_component = Component(**new_component_dict)
        
        arr_components.append(new_component)
    
    Component.objects.bulk_create(arr_components)

def importBillOfMaterials():
    reader = csv.DictReader(open('../data/bill_of_materials.csv'))

    for row in reader:
        tube_assembly_id = int(row['tube_assembly_id'].replace('TA-',''))
        new_tybe_assembly = TubeAssembly(pk=tube_assembly_id)
        new_tybe_assembly.save()

        for i in range(1,9):
            str_component_id = "component_id_%s" % i
            str_quantity = "quantity_%s" % i

            if row[str_component_id] == "NA":
                continue

            component_id = int(row[str_component_id].replace('C-',''))
            quantity = int(row[str_quantity])

            
            try:
                component = Component.objects.get(pk=component_id)
            except Component.DoesNotExist:
                print("component does not exist: %s " % component_id)
                continue

            aseembly_component = AssemblyComponent(tube_assembly=new_tybe_assembly, component=component, quantity=quantity)
            aseembly_component.save()

def importPriceQuote():
    reader = csv.DictReader(open('../data/price_quote.csv'))

    arr_price_quote = []
    for row in reader:
        new_price_quote_dict = row
        tube_assembly_id = int(row['tube_assembly_id'].replace('TA-',''))
        supplier_id = int(row['supplier'].replace('S-',''))

        new_price_quote_dict.update({k:False for k,v in row.items() if v == 'No' })
        new_price_quote_dict.update({k:True for k,v in row.items() if v == 'Yes' })

        supplier, created = Supplier.objects.get_or_create(pk=supplier_id, name=row['supplier'])
        del row['supplier']
        del row['tube_assembly_id']
        try:
            tube_assembly = TubeAssembly.objects.get(pk=tube_assembly_id)
        except Component.DoesNotExist:
            print("tube assembly does not exist: %s " % tube_assembly_id)
            continue   


        new_price_quote_dict.update({'tube_assembly': tube_assembly, 'supplier': supplier})

        

        new_price_quote = PriceQuote(**new_price_quote_dict)
        
        arr_price_quote.append(new_price_quote)

        if len(arr_price_quote) > 1000:
            PriceQuote.objects.bulk_create(arr_price_quote)
            arr_price_quote = []

    if len(arr_price_quote)>0:
        PriceQuote.objects.bulk_create(arr_price_quote)
