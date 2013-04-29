from ajax_select import LookupChannel
from django.utils.html import escape
from django.db.models import Q
from dasdemo.models import Country

my_flags = "http://localhost:8000/static/flags/"

class CountryLookup(LookupChannel):

    model = Country

    def get_query(self,q,request):
        return Country.objects.filter(Q(name__icontains=q) | Q(short__istartswith=q)).order_by('name')

    def get_result(self,obj):
        u""" result is the simple text that is the completion of what the Country typed """
        return obj.name

    def format_match(self,obj):
        """ (HTML) formatted item for display in the dropdown """
        return self.format_item_display(obj)


    def format_item_display(self,obj):
        """ (HTML) formatted item for displaying item in the selected deck area """
        flags_url = my_flags + obj.short +".png"
        img_html = '<img src="%s">' % flags_url
        return u"%s<div><i>%s</i></div>" % (escape(obj.name), img_html)

#Note that raw strings should always be escaped with the escape() function