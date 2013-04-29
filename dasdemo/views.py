# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson as json

from models import Country, Cars

from form import CarForm
from django.forms.models import inlineformset_factory

def main(request):
	return HttpResponse("booo")

def demo(request):

	if request.method == 'GET':
		our_form = CarForm()
		context = {"form": our_form}
		return render(request, "dasdemo/dasdemo.html", context)
	else:
		#CarInlineFormset = inlineformset_factory(Cars, Country, form = CarForm)
		get_form = CarForm(request.POST)
		


		import pdb; pdb.set_trace()
		if get_form.is_valid():
			#import pdb; pdb.set_trace()
			get_form.save()
			

			#form.country = Country.object.get(pk = request.POST.get('country'))
			#fixed_form.save()
			return HttpResponse("thanks!!")
		else:
			return render(request, "dasdemo/dasdemo.html", context)