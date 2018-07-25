from import_export import resources
from ..models import Component

class ComponentResource(resources.ModelResource):

    class Meta:
        model = Component