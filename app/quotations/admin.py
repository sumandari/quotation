from django.contrib import admin

from .models import AddOnPrice, Customer, Vehicle, Quotation


class AddOnPriceAdmin(admin.ModelAdmin):
    """Coverage admin model."""
    list_display = ('windscreen', 'passanger_liability', 'others')
    fields = ('windscreen', 'passanger_liability', 'others')


class CustomerAdmin(admin.ModelAdmin):
    """Coverage admin model."""
    list_display = ('name', 'email', 'mobile_number')
    fields = ('name', 'email', 'mobile_number')


class QuotationAdmin(admin.ModelAdmin):
    """Quotation admin model."""

    list_display = (
        'number', 'vehicle',
        'windscreen', 'passanger_liability', 'others',
        'price', 'created_at'
    )
    fields = ('number', 'vehicle',
              'windscreen', 'passanger_liability', 'others',
              'price')


class VehicleAdmin(admin.ModelAdmin):
    """Vehicle admin model."""
    list_display = ('customer', 'year_make', 'model', 'number', 'price')
    fields = ('customer', 'year_make', 'model', 'number', 'price')


admin.site.register(AddOnPrice, AddOnPriceAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Quotation, QuotationAdmin)
admin.site.register(Vehicle, VehicleAdmin)
