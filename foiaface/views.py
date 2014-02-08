from django.shortcuts import render_to_response
from models import Jurisdiction

def home(request):
    jurisdictions = Jurisdiction.objects.all()
    return render_to_response('index.html', {'jurisdictions': jurisdictions})


def subdivisions(request, j_id):
    subdivisions = Jurisdiction.objects.filter(parent_jurisdiction=j_id)
    return render_to_response('subdivisions.html', {'subdivisions': subdivisions})
