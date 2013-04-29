# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson as json

from models import Country, Cars

from form import CarForm, CarForm2

def main(request):
	return HttpResponse("booo")

def demo(request):

	if request.method == 'GET':
		our_form = CarForm()
		context = {"form": our_form}
		return render(request, "dasdemo/dasdemo.html", context)
	else:

		get_form = CarForm(request.POST)
		


		#import pdb; pdb.set_trace()
		if get_form.is_valid():
			#import pdb; pdb.set_trace()
			get_form.save()

			return HttpResponse("thanks!!")
		else:
			return render(request, "dasdemo/dasdemo.html", context)

def demo2(request):

	if request.method == 'GET':
		our_form = CarForm2()
		context = {"form": our_form}
		return render(request, "dasdemo/dasdemo2.html", context)
	else:

		get_form = CarForm2(request.POST)

		#import pdb; pdb.set_trace()
		if get_form.is_valid():
			#import pdb; pdb.set_trace()
			get_form.save()

			return HttpResponse("thanks!!")
		else:
			return render(request, "dasdemo/dasdemo2.html", context)