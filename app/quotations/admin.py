from django.contrib import admin

from .models import AddOnPrice, Quotation


@admin.register(AddOnPrice)
class AddOnPriceAdmin(admin.ModelAdmin):
    """Coverage admin model."""
    list_display = ('windscreen', 'passanger_liability', 'others')
    fields = ('windscreen', 'passanger_liability', 'others')



@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    """Quotation admin model."""

    list_display = (
        'number', 'created_at',
        'name', 'email',
        'vehicle_price', 'vehicle_model', 'vehicle_year',
        'with_addon',
        'price',
    )
    fields = (
        'number',
        'name', 'email', 'mobile_number',
        'vehicle_year', 'vehicle_model', 'vehicle_number', 'vehicle_price',
        'cov_windscreen', 'cov_passanger_liability', 'cov_others',
        'price'
    )
    search_fields = ['email', 'number', 'vehicle']
    actions = ['send_email']

    def with_addon(self, obj):
        if 'yes' in [obj.cov_windscreen,
                     obj.cov_passanger_liability,
                     obj.cov_others]:
            return 'yes'
        return 'no'

    @admin.action(description="Send to user’s email")
    def send_email(self, request, queryset):
        # TODO
        # send to user
        for q in queryset:
            print(f'sending quotation {q.number} to {q.email}')
