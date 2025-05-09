from django.contrib import admin
from .models import Product, Stock

class StockInline(admin.TabularInline):
    model = Stock
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [StockInline]
    list_display = ('name', 'price', 'get_stock_quantity')
    
    def get_stock_quantity(self, obj):
        # Safely get the stock quantity or return 0 if no stock exists
        stock = obj.stocks.first()  # Using the related_name
        return stock.quantity if stock else 0
    get_stock_quantity.short_description = 'Stock Quantity'

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'last_updated')
    list_filter = ('product',)