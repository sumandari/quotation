from decimal import Decimal
from slugify import slugify
from weasyprint import HTML

from django.http import Http404, HttpResponse
from django.core.mail import send_mail, EmailMessage
from django.forms.models import model_to_dict
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, FormView
from django.template.loader import render_to_string
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
            quotation.cov_windscreen = addons[0]
        if form.cleaned_data['passenger_liability'] == 'yes':
            addon_total += addons[1]
            quotation.cov_passanger_liability = addons[1]
        if form.cleaned_data['others'] == 'yes':
            addon_total += addons[2]
            quotation.cov_others = addons[2]

        quotation.price = (
            (Decimal(2/100) * Decimal(quotation.vehicle_price)) +
            Decimal(addon_total)
        )

        quotation.number = self.get_customer_quot_number(
            quotation.email, quotation.name)
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

    def get_customer_quot_number(self, email, name):
        email_count =  Quotation.objects.filter(email=email).count()
        name_slug = slugify(name)
        return f'MI-{name_slug}-{email_count}'


class QuotationDetailView(DetailView):

    context_object_name = 'quotation'
    model = Quotation
    template_name = 'quotations/detail.html'

    def get_context_data(self, **kwargs):
        context = super(QuotationDetailView, self).get_context_data(**kwargs)
        context['basic_price'] = round(self.object.vehicle_price * Decimal(2/100), 2)
        return context


class QuotationSendEmailPDFView(QuotationDetailView):
    template_name = 'quotations/pdf.html'

    def render_to_response(self, context, **response_kwargs):
        response = super(QuotationSendEmailPDFView, self).render_to_response(context, **response_kwargs)
        response.render()
        pdf_response = HttpResponse(content_type='application/pdf')
        pdf_response['Content-Disposition'] = 'filename={}.pdf'.format(self.object.number)
        html_object = HTML(
            string=response.content,
            base_url='file://',
        )
        html_object.write_pdf(
            pdf_response,
            stylesheets=['https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css']
        )

        # send email
        send_quotation(self.object, self.template_name)
        return pdf_response


def send_quotation(obj, template):
    ctx = model_to_dict(obj)
    pdf = HTML(string=render_to_string(template, ctx)).write_pdf()
    email = EmailMessage(
        'Motor Insurance Quotation',
        'Thank you for your inquiry. Please find the quotation attached.',
        'from@example.com',
        [obj.email],
        headers={'Message-ID': 'foo'},
    )
    email.attach(f'{obj.number}.pdf', pdf, 'application/pdf')
    email.content_subtype = 'pdf'
    email.encoding = 'us-ascii'
    email.send()
