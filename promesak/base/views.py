from django.shortcuts import render
from django.shortcuts import get_object_or_404
from promesak.base.models import Promise
from promesak.base.models import Party


def index(request):
    h = {}
    h['parties'] = Party.objects.all().order_by('?')
    h['promises'] = Promise.objects.all().order_by('-date_promised')

    return render(
        request,
        'base/index.html',
        h
    )


def party_view(request, slug):
    h = {}
    h['party'] = get_object_or_404(Party, slug=slug)
    h['promises'] = h['party'].promise_set.all().order_by('-date_promised')
    return render(
        request,
        'base/party_view.html',
        h
    )


def promise_view(request, slug):
    h = {}
    h['promise'] = get_object_or_404(Promise, slug=slug)
    return render(
        request,
        'base/promise_view.html',
        h
    )
