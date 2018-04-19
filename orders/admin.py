from django.contrib import admin

# Register your models here.

from .models import Menu, Customer, Order

# to display all columns on the admin site:
class MenuAdmin(admin.ModelAdmin):
    list_display = ('item', 'sub_item', 'price_small', 'price_large')

    def item(self, obj):
        return obj.item

    def sub_item(self, obj):
        return obj.sub_item

    def price_small(self, obj):
        return obj.price_small

    def price_large(self, obj):
        return obj.price_large

class CustomerAdmin(admin.ModelAdmin):
    customer_display = ('first', 'last')

    def first(self, obj):
        return obj.first

    def last(self, obj):
        return obj.last

class OrderAdmin(admin.ModelAdmin):
#    order_display = ('order_item', 'order_customer', 'order_total')
    order_display = ('item', 'sub_item', 'price_small', 'price_large', 'order_customer', 'order_total')

    def item(self, obj):
        return obj.item

    def sub_item(self, obj):
        return obj.sub_item

    def price_small(self, obj):
        return obj.price_small

    def price_large(self, obj):
        return obj.price_large

    #def order_item(self, obj):
    #    return obj.order_item.item

    def order_customer(self, obj):
        return obj.order_customer

    def order_total(self, obj):
        return obj.order_total


admin.site.register(Menu, MenuAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
