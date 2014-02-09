from django.shortcuts import render_to_response
from models import Jurisdiction

def home(request):
    jurisdictions = Jurisdiction.objects.filter(parent_jurisdiction=None)
    return render_to_response('index.html', {'jurisdictions': jurisdictions})

def letter(request, jurisdiction):
    jurisdiction = Jurisdiction.objects.get(pk=jurisdiction)
    return render_to_response('letter.html', {'jurisdiction':jurisdiction})

def subdivisions(request, parent):
    subdivisions = Jurisdiction.objects.filter(parent_jurisdiction=parent)
    if subdivisions:
        return render_to_response('subdivisions.html', 
            {'subdivisions': subdivisions})
    else:
        return render_to_response('letter.html', {'jurisdiction':parent})

def resources(request):
    return render_to_response('resources.html')
