from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='name', required=True, max_length=100)
    description = forms.CharField(label='description', max_length=1000)
    price = forms.DecimalField(label='price', localize=True)

