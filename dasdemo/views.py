# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson as json


def main(request):
	return HttpResponse("booo")