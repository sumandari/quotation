from django.contrib import admin

from .models import AddOnPrice, Customer, Vehicle, Quotation


@admin.register(AddOnPrice)
class AddOnPriceAdmin(admin.ModelAdmin):
    """Coverage admin model."""
    list_display = ('windscreen', 'passanger_liability', 'others')
    fields = ('windscreen', 'passanger_liability', 'others')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Coverage admin model."""
    list_display = ('name', 'email', 'mobile_number')
    fields = ('name', 'email', 'mobile_number')


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    """Vehicle admin model."""
    list_display = ('customer', 'year_make', 'model', 'number', 'price')
    fields = ('customer', 'year_make', 'model', 'number', 'price')


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    """Quotation admin model."""

    list_display = (
        'number',
        'get_customer', 'vehicle',
        'windscreen', 'passanger_liability', 'others',
        'price', 'created_at'
    )
    fields = (
        'number', 'vehicle',
        'windscreen', 'passanger_liability', 'others',
        'price'
    )
    search_fields = ['vehicle__customer__email', 'number', 'vehicle']
    actions = ['send_email']

    def get_customer(self, obj):
        return obj.vehicle.customer

    @admin.action(description="Send to user’s email")
    def send_email(self, request, queryset):
        # TODO
        # send to user
        for q in queryset:
            print(f'sending quotation {q.number} to {q.vehicle.customer.email}')
