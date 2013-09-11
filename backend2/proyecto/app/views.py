# Create your views here.

from django.http import HttpResponse

def home(request):
	return HttpResponse("Hola Mundo :) %s" % request)

	
def post(request, num):
	if(int(num) < 10):
		return HttpResponse("Menor : %i" % int(num))
	else:
		return HttpResponse("Mayor: %i" % int(num))
	