from django.urls import path

from .views import QuotationDetailView, QuotationFormView, QuotationSendEmailPDFView


urlpatterns = [
    path('', QuotationFormView.as_view(), name='quotation_create'),
    path('quotation/<int:pk>/', QuotationDetailView.as_view(), name='quotation_detail'),
    path('quotation/send_email/<int:pk>/', QuotationSendEmailPDFView.as_view(), name='quotation_pdf'),
]
