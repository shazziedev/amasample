from django.contrib import admin

from .models import Cart

class CartAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity')
    list_filter = (['item'])
    #search_fields = ( 'item', 'user' )
    ordering = ( 'timestamp','quantity')
    filter_horizontal = ()


admin.site.register(Cart,CartAdmin)

