from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuotationDetail, QuotationEmail

urlpatterns = [
    path('api/quotation/<int:pk>/', QuotationDetail.as_view()),
    path('api/quotation/<int:pk>/email', QuotationEmail.as_view(), name='api_email'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
