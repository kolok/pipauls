from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class ProductNameForm(forms.Form):
    name = forms.CharField(help_text="Enter the name of the product", required=True, min_length=3)

    def clean_name(self):
        data = self.cleaned_data['name']

        # Check if a date is not in the past.
        if data.find('e') != -1:
            raise ValidationError(_('`e` is a forbidden character'))

        return data


class ProductForm(forms.Form):
    name = forms.CharField(label='name', required=True, max_length=100)
    description = forms.CharField(label='description', max_length=1000)
    price = forms.DecimalField(label='price', localize=True)