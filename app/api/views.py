from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from quotations.models import Quotation
from quotations.views import send_quotation
from api.serializers import QuotationSerializer

class QuotationDetail(APIView):

    def get_object(self, pk):
        try:
            return Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quotation = self.get_object(pk)
        serializer = QuotationSerializer(quotation)
        return Response(serializer.data)


class QuotationEmail(APIView):

    def get_object(self, pk):
        try:
            return Quotation.objects.get(pk=pk)
        except Quotation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        quotation = self.get_object(pk)
        send_quotation(quotation, 'quotations/pdf.html')
        return Response({}, status=status.HTTP_204_NO_CONTENT)
