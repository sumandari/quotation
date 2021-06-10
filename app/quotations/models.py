from django.db import models
from django.core.validators import MinValueValidator


class Customer(models.Model):
    name = models.CharField(
        help_text="Customer's name.",
        max_length=64,
        null=False,
    )
    email = models.EmailField(
        help_text="Customer's email.",
        max_length=254,
        null=False,
        unique=True,
    )
    mobile_number = models.CharField(
        help_text="Customer's mobile number.",
        max_length=20,
        null=True
    )

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    year_make = models.IntegerField(
        help_text="Vehicle year make.",
    )
    model = models.CharField(
        help_text='Vehicle model.',
        max_length=100
    )
    number = models.CharField(
        help_text='Vehicle No.',
        max_length=20,
        unique=True,
    )
    price = models.DecimalField(
        help_text='Vehicle price in RM',
        max_digits=12,
        decimal_places=2,
        default=100000.00,
        validators=[MinValueValidator(30000.00)]
    )

    def __str__(self):
        return f'{self.number}: {self.model} {self.year_make}'


class Quotation(models.Model):
    """Quotation Model."""

    number = models.CharField(
        help_text='Quotation number.',
        max_length=20
    )
    price = models.DecimalField(
        help_text='Quotation price.',
        max_digits=12,
        decimal_places=2
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    YES_NO_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No')
    ]
    windscreen = models.CharField(
        help_text='Windscreen coverage',
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no'
    )
    passanger_liability = models.CharField(
        help_text='Passanger Liability coverage',
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no'
    )
    others = models.CharField(
        help_text='Flood, Windstorm, Landslide or Subsidence coverage',
        max_length=3,
        choices=YES_NO_CHOICES,
        default='no'
    )
    vehicle = models.ForeignKey(
        Vehicle,
        on_delete=models.CASCADE,
        null=False
    )


class AddOnPrice(models.Model):
    """Default Add on price model.

    Insurance agent can modify the additional coverage prices
    """
    windscreen = models.DecimalField(
        help_text='Windscreen addon price.',
        max_digits=10,
        decimal_places=2
    )
    passanger_liability = models.DecimalField(
        help_text='Passanger liability addon price.',
        max_digits=10,
        decimal_places=2
    )
    others = models.DecimalField(
        help_text='Flood, Windstorm, Landslide or Subsidence addon price.',
        max_digits=10,
        decimal_places=2
    )
