from django.test import TestCase

from .models import Quotation

class TestQuotationModel(TestCase):
    """Test Quotation models."""

    def test_create_quotation_without_addon(self):
        quot = Quotation.objects.create(
            price=1234.56,
            name='Customer Test',
            email='email@example.com',
            mobile_number='123456789',
            vehicle_year=2000,
            vehicle_model='Savvy',
            vehicle_number='CAR12345',
            vehicle_price=123456.78,
        )
        self.assertEqual(
            quot.name, 'Customer Test'
        )
        self.assertEqual(
            quot.vehicle_year, 2000
        )
        self.assertEqual(
            quot.cov_windscreen, 'no'
        )
        self.assertEqual(
            quot.cov_passanger_liability, 'no'
        )
        self.assertEqual(
            quot.cov_others, 'no'
        )
        self.assertEqual(
            quot.price, 1234.56
        )

    def test_create_quotation_with_addon(self):
        quot = Quotation.objects.create(
            price=1234.56,
            name='Customer Test',
            email='email@example.com',
            mobile_number='123456789',
            vehicle_year=2000,
            vehicle_model='Savvy',
            vehicle_number='CAR12345',
            vehicle_price=123456.78,
            cov_windscreen='yes',
            cov_others='yes'
        )
        self.assertEqual(
            quot.cov_windscreen, 'yes'
        )
        self.assertEqual(
            quot.cov_passanger_liability, 'no'
        )
        self.assertEqual(
            quot.cov_others, 'yes'
        )
