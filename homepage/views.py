from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def index(request):
    #member_list = Member.objects.order_by('name')
    context = {}
    return render(request, 'homepage/index.html', context)

