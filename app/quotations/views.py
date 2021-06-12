from decimal import Decimal
from slugify import slugify

from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, FormView
from django.urls import reverse

from .forms import QuotationForm
from .models import AddOnPrice, Quotation


class QuotationFormView(FormView):
    template_name = 'quotations/upload_form.html'
    form_class = QuotationForm
    model = Quotation

    def form_valid(self, form):
        quotation = self.model(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            mobile_number=form.cleaned_data['mobile_number'],
            vehicle_year=form.cleaned_data['vehicle_year'],
            vehicle_model=form.cleaned_data['vehicle_model'],
            vehicle_number=form.cleaned_data['vehicle_number'],
            vehicle_price=form.cleaned_data['vehicle_price'],
        )
        addons = self.get_add_on()
        addon_total = 0
        if form.cleaned_data['windscreen'] == 'yes':
            addon_total += addons[0]
        if form.cleaned_data['passanger_liability'] == 'yes':
            addon_total += addons[1]
        if form.cleaned_data['others'] == 'yes':
            addon_total += addons[2]

        quotation.price = (Decimal(2/100) * Decimal(quotation.vehicle_price)) + Decimal(addon_total)
        quotation.save()
        return redirect(reverse('quotation_detail', args=(quotation.id,)))

    def get_add_on(self):
        addon = AddOnPrice.objects.last()
        if not addon:
            addon_windscreen, addon_passanger_liability, addon_others = (0, 0, 0)
        else:
            addon_windscreen = addon.windscreen
            addon_passanger_liability = addon.passanger_liability
            addon_others = addon.others
        return addon_windscreen, addon_passanger_liability, addon_others


class QuotationDetailView(DetailView):

    context_object_name = 'quotation'
    model = Quotation
    template_name = 'quotations/detail.html'
