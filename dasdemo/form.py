from django import forms

from ajax_select import make_ajax_field

from models import Cars, Country

class CarForm(forms.ModelForm):

	brand = forms.CharField()
	name = forms.CharField()
	country = make_ajax_field(Cars, 'country', 'country')

	class Meta:
		model = Cars


class CarForm2(forms.ModelForm):

	brand = forms.CharField()
	name = forms.CharField()
	country = make_ajax_field(Cars, 'country', 'custom_country')

	class Meta:
		model = Cars