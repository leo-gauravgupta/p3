from django.db import models

# Create your models here.

class Menu(models.Model):
    item = models.CharField(max_length=64, blank=True, null=True)
    sub_item = models.CharField(max_length=64, blank=True, null=True)
    price_small = models.FloatField(blank=True, null=True)
    price_large = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.item} {self.sub_item} {self.price_small} {self.price_large}"

class Customer(models.Model):
    first = models.CharField(max_length=64, blank=True, null=True)
    last = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.first} {self.last}"

#class Order(models.Model):
class Order(Menu):
    #order_item = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="orders").objects.get(item)
    #order_item = models.Menu.item()
    #item = Menu.item
    #sub_item = Menu.sub_item
    #price_small = Menu.price_small
    #price_large = Menu.price_large
    order_customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="customers_waiting", blank=True, null=True)
    order_total = models.FloatField(blank=True, null=True)

    def __str__(self):
        #return f"{self.id} - {self.order_item} for {self.order_customer} total {self.order_total}"
        return f"{self.id} - {self.item} {self.sub_item} for {self.order_customer} total {self.order_total}"
