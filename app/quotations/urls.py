from django.urls import path

from .views import QuotationCreateView, QuotationDetailView


urlpatterns = [
    path('', QuotationCreateView.as_view(), name='quotation_create'),
    path('quotation/<int:pk>/', QuotationDetailView.as_view(), name='quotation_detail')
]
