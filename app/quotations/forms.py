from django import forms

from .models import Quotation

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Fieldset, Field, Layout, Row, Submit



class QuotationForm(forms.ModelForm):

    class Meta:
        model = Quotation
        fields = (
            'name',
            'email',
            'mobile_number',

            'vehicle_year',
            'vehicle_model',
            'vehicle_number',
            'vehicle_price',

            'cov_windscreen',
            'cov_passanger_liability',
            'cov_others'
        )

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
                    Column('cov_windscreen', css_class='form-group col-md-4'),
                    Column('cov_passanger_liability', css_class='form-group col-md-4'),
                    Column('cov_others', css_class='form-group col-md-4'),
                ),
                css_class='mb-5'
            ),

            Submit('submit', 'Submit', css_class='btn btn-primary btn-block')
        )
        self.helper.html5_required = False
        super(QuotationForm, self).__init__(*args, **kwargs)
        # change label
        self.fields['cov_windscreen'].label = 'Windscreen'
        self.fields['cov_passanger_liability'].label = 'Passanger Liability'
        self.fields['cov_others'].label = 'Flood, Windstorm, Landslide or Subsidence '
