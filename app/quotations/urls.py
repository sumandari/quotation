from django.urls import path

from .views import QuotationDetailView, QuotationFormView


urlpatterns = [
    path('', QuotationFormView.as_view(), name='quotation_create'),
    path('quotation/<int:pk>/', QuotationDetailView.as_view(), name='quotation_detail')
]
