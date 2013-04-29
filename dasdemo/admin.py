from django.contrib import admin
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
from typeahead.models import *
from dasdemo.models import Cars

class CountryAdmin(admin.ModelAdmin):
	pass

admin.site.register(Country, CountryAdmin)

class CarsAdmin(AjaxSelectAdmin):
	form = make_ajax_form(Cars, {'country': 'country'})
admin.site.register(Cars, CarsAdmin)

