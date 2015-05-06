from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from promesak.base.models import Promise


# Create your views here.
def index(request):
    h = {}
    h['promises'] = Promise.objects.all().order_by('-date_promised')
    return render(
        request,
        'base/index.html',
        h
    )
