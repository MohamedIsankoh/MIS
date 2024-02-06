from django.contrib import admin
from .forms import *

# Register your models here.

from .models import *

class StockCreateAdmin(admin.ModelAdmin):
   list_display = ['category', 'item_name', 'quantity']
   form = StockCreateForm
   list_filter = ['category']
   search_fields = ['category', 'item_name']


# Invoice Code start
class InvoiceAdmin(admin.ModelAdmin):
   list_display = ['name', 'invoice_number', 'invoice_date']
   form = InvoiceForm
   list_filter = ['name']
   search_fields = ['name', 'invoice_number']




# Invoice code end
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(Invoice, InvoiceAdmin)
