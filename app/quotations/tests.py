from django.test import TestCase

from .models import Customer, Vehicle, Quotation

class TestQuotationModel(TestCase):
    """Test Quotation models."""

    def setUp(self):
        self.customer = Customer.objects.create(
            name='Customer Test',
            email='email@example.com',
            mobile_number='123456789'
        )
        self.vehicle = Vehicle.objects.create(
            customer=self.customer,
            year_make=2000,
            model='Savvy',
            number='CAR12345',
            price=123456.78
        )

    def test_str_customer_vehicle(self):
        self.assertEqual(
            self.customer.__str__(), 'Customer Test'
        )
        self.assertEqual(
            self.vehicle.__str__(),
            'CAR12345: Savvy 2000'
        )

    def test_create_quotation_without_addon(self):
        quot = Quotation.objects.create(
            vehicle=self.vehicle,
            price=1234.56
        )
        self.assertEqual(
            quot.vehicle.customer, self.customer
        )
        self.assertEqual(
            quot.vehicle.year_make, 2000
        )
        self.assertEqual(
            quot.windscreen, 'no'
        )
        self.assertEqual(
            quot.passanger_liability, 'no'
        )
        self.assertEqual(
            quot.others, 'no'
        )
        self.assertEqual(
            quot.price, 1234.56
        )

    def test_create_quotation_with_addon(self):
        quot = Quotation.objects.create(
            vehicle=self.vehicle,
            price=1234.56,
            windscreen='yes',
            others='yes'
        )
        self.assertEqual(
            quot.windscreen, 'yes'
        )
        self.assertEqual(
            quot.passanger_liability, 'no'
        )
        self.assertEqual(
            quot.others, 'yes'
        )
