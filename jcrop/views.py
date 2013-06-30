# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import simplejson as json

from PIL import Image
import urllib2 as urllib
import cStringIO
import io

from django.core.files.storage import default_storage as storage

from .models import Photo

def jcrop(request):
	if request.method == 'GET':
		return render(request, "jcrop/jcrop.html")
	else:
		#get image parameters for cropping
		x = request.POST.get('x')
		y = request.POST.get('y')
		width = request.POST.get('width')
		height = request.POST.get('height')
		image_url = request.POST.get('image')

		#if the image url is not available, abort mission..
		if not image_url:
			return HttpResponse("no image..")		

		#open image url, and crop image
		file = io.BytesIO(urllib.urlopen(image_url).read())
		img = Image.open(file)
		box = (int(x), int(y), int(x) + int(width), int(y) + int(height))
		cropped_image = img.crop(box)

		format = 'png'  # You need to set the correct image format here
		response = HttpResponse(mimetype="image/JPEG")
    	cropped_image.save(response, format)

    	fh = storage.open("cropped_image" + ".png", "w")
    	cropped_image.save(fh, format)
    	fh.close()
    	
    	return response
    	
