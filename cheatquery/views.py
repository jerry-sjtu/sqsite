from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from cheatquery.models import CommonQuery, SeCheatkeyword
from cheatquery.forms import CheatQueryFilterForm
from django import forms
from django.db.models import Count, Sum, Avg, Max
import json
import datetime

def index(request):
    context = dict()
    if request.method == 'POST':
        form = CheatQueryFilterForm(request.POST)
        if form.is_valid():
            context['result_list'] = cheat_query(form)
    else:
        form = CheatQueryFilterForm(business=1, fromdate=datetime.datetime.now, todate=datetime.datetime.now)
    context['form'] = form
    return render(request, 'cheatquery/index.html', context)

def cheat_query(form):
    business = form.cleaned_data['business']
    fromdate = form.cleaned_data['fromdate']
    todate = form.cleaned_data['todate']
    city = form.cleaned_data['city_list']

    q = SeCheatkeyword.objects.filter(business=business,adddate__gte=fromdate, adddate__lte=todate,  ischeat=1)
    q = q.values('keyword', 'cityid').order_by('-searchnum')
    if city != None and int(city) != -1: 
        q = q.filter(cityid=city)
    q = q.annotate(searchnum=Sum('searchnum'), crosscitynum=Sum('crosscitynum'), clickedsearchnum=Sum('clickedsearchnum'), hitnum=Max('hitnum'))
    print q.query
    return fill_ratio(q)

def fill_ratio(result_list):
    linenum = 1
    for item in result_list:
        item['linenum'] = linenum
        item['clickrate'] = divide(float(item['clickedsearchnum']), item['searchnum'])
        linenum += 1
    return result_list

def divide(num1, num2):
    if num2 == 0:
        return 0
    else:
        return '{0:.3f}'.format(float(num1) / num2)