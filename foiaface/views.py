from django.shortcuts import render_to_response
from models import Jurisdiction

def home(request):
    jurisdictions = Jurisdiction.objects.filter(parent_jurisdiction=None)
    return render_to_response('index.html', {'jurisdictions': jurisdictions})

def subdivisions(request, parent):
    subdivisions = Jurisdiction.objects.filter(parent_jurisdiction=parent)
    return render_to_response('subdivisions.html', 
    	{'subdivisions': subdivisions})
