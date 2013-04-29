# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson as json
from django.db.models import Q

from dasdemo.models import Country


def main(request):
	return render(request, "typeahead/typeahead.html")

def api(request):
	qry  =  request.GET.get('q')
	res = {"stat": "error"}
	if qry:
		res = Country.objects.filter(name__istartswith = qry).values('id','name')
		res = list(res)
	
	return HttpResponse(json.dumps(res), mimetype="application/json")


def api2(request):
	qry  =  request.GET.get('q')
	res = {"stat": "error"}
	data ={}

	if qry:
		res = Country.objects.filter(name__istartswith = qry).values('id','name')
		res = list(res)
		data['suggestions'] = res

	
	
	if data:
		return HttpResponse(json.dumps(data), mimetype = 'application/json')
	else:
		return HttpResponse(json.dumps(res), mimetype = 'application/json')


def api3(request):
	qry  =  request.GET.get('query')
	res = {"stat": "error"}
	data ={}
	suggestions = []

	if qry:
		res = Country.objects.filter(name__istartswith = qry)
		
		
		
		
		for country in res:
			temp = {}
			temp['id'] = country.id
			temp['value'] = country.name #res[i]['name']
			temp['data'] = country.name #res[i]['id']
			suggestions.append(temp)

		data['query'] = qry
		data['suggestions'] = suggestions

	
	
	if data:
		return HttpResponse(json.dumps(data), mimetype = 'application/json')
	else:
		return HttpResponse(json.dumps(res), mimetype = 'application/json')