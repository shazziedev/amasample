from django.contrib import admin

from .models import *

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'seller' ,'location' , 'is_sold','timestamp',)
    list_filter = (['name'])
#    search_fields = ( 'name', 'seller' )
    ordering = ('timestamp',)
    filter_horizontal = ()
    actions = ['is_sold', 'is_available']

    def is_sold(self, request, queryset):
    	queryset.update(is_sold=True)

    def is_available(self, request, queryset):
    	queryset.update(is_sold=False)


admin.site.register(Items,ItemAdmin)




admin.site.register(Category)