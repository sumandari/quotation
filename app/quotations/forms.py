from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Fieldset, Field, Layout, Row, Submit


YES_NO_CHOICES = [
    ('yes', 'Yes'),
    ('no', 'No')
]


class QuotationForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=64)
    email = forms.EmailField(label='Your email')
    mobile_number = forms.CharField(label='Your mobile number', max_length=64)

    vehicle_year = forms.IntegerField(label='Year make', min_value=1980)
    vehicle_model = forms.CharField(label='Model', max_length=100)
    vehicle_number = forms.CharField(label='Number', max_length=20)
    vehicle_price = forms.FloatField(label='Vehicle price', initial=100000.00, min_value=30000.00)

    windscreen = forms.ChoiceField(choices=YES_NO_CHOICES)
    passenger_liability = forms.ChoiceField(choices=YES_NO_CHOICES)
    others = forms.ChoiceField(choices=YES_NO_CHOICES)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Customer Data',
                Field('name', css_class='form-control'),
                Field('email', css_class='form-control'),
                Field('mobile_number', css_class='form-control'),
                css_class='mb-5'
            ),

            Fieldset(
                'Vehicle',
                Field('vehicle_model', css_class='form-control'),
                Field('vehicle_price', css_class='form-control'),
                Row(
                    Column('vehicle_number', css_class='form-group col-md-6'),
                    Column('vehicle_year', css_class='form-group col-md-6')
                ),
                css_class='mb-5'
            ),

            Fieldset(
                'Coverage',
                Row(
                    Column('windscreen', css_class='form-group col-md-4'),
                    Column('passenger_liability', css_class='form-group col-md-4'),
                    Column('others', css_class='form-group col-md-4'),
                ),
                css_class='mb-5'
            ),

            Submit('submit', 'Submit', css_class='btn btn-primary btn-block')
        )
        self.helper.html5_required = False
        super(QuotationForm, self).__init__(*args, **kwargs)
