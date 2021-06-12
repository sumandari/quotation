from decimal import Decimal
from slugify import slugify

from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.urls import reverse

from .forms import QuotationForm
from .models import AddOnPrice, Quotation


class QuotationCreateView(CreateView):

    template_name = 'quotations/upload_form.html'
    form_class = QuotationForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        addon = AddOnPrice.objects.last()
        if not addon:
            addon_windscreen, addon_passanger_liability, addon_others = (0, 0, 0)
        else:
            addon_windscreen = addon.windscreen
            addon_passanger_liability = addon.passanger_liability
            addon_others = addon.others
        addon_total = addon_windscreen + addon_passanger_liability + addon_others
        obj.price = (Decimal(2/100) * obj.vehicle_price) + addon_total

        # quotation numbering pattern
        # - start from MI (Motor Insurance)
        # - 10 first chars of user's name with unique email
        # - number of user's submitted form
        email_count = Quotation.objects.filter(email=obj.email).count()
        obj.number = f'MI-{slugify(obj.name)[:10]}-{email_count + 1}'
        obj.save()
        return redirect(reverse('quotation_detail', args=(obj.id,)))


class QuotationDetailView(DetailView):

    context_object_name = 'quotation'
    model = Quotation
    template_name = 'quotations/detail.html'

