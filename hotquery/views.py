from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from kpi.models import CommonQuey, FormatHelper, MathHelper
from hotquery.models import SeQueryanalysis
from hotquery.forms import HotqueryFilterForm
from django.conf import settings
from django.db.models import Count, Sum, Avg
import json

def index(request):
    context = dict()
    if request.method == 'POST':
        form = HotqueryFilterForm(request.POST)
        if form.is_valid():
            result_list = keyword_query(form)
            context['keyword_result'] = result_list
            form.init_fromdate = form.cleaned_data['fromdate'].strftime('%Y-%m-%d')
            form.init_todate = form.cleaned_data['todate'].strftime('%Y-%m-%d')
            #form.algo_list = get_algo_version(init_business, init_fromdate, init_todate)
    else:
        form = HotqueryFilterForm()
    context['form'] = form
    return render(request, 'hotquery/index.html', context)

def keyword_query(form):
    business = form.cleaned_data['business']
    fromdate = form.cleaned_data['fromdate']
    todate = form.cleaned_data['todate']
    algo = form.cleaned_data['algo_list']
    city = form.cleaned_data['city_list']

    q = SeQueryanalysis.objects.filter(businesstype=business,statdate__gte=fromdate,statdate__lte=todate,
        keywordtype=0)
    q = q.values('businesstype', 'cityid', 'keyword')
    if algo != None and algo != 'all': 
        q = q.filter(algoversion=algo)
    if city != None and int(city) != -1: 
        q = q.filter(cityid=city)
    q = q.annotate(searchnum=Sum('searchnum'), clicknum=Sum('clicknum'), clickedsearchnum=Sum('clickedsearchnum'),
        clickpos=Sum('clickpos'), dropdownnum=Sum('dropdownnum')).order_by('-searchnum')[:500]
    #print q.query
    q = fill_ratio(q)
    return fill_date_info(q, fromdate, todate)

def fill_date_info(result_list, from_date, to_date):
    for item in result_list:
        item['from_date']  = from_date
        item['to_date'] = to_date
    return result_list

def fill_ratio(result_list):
    i = 1
    for item in result_list:
        item['linenum'] = i
        i += 1
        item['clickrate'] = MathHelper.divide(float(item['clickedsearchnum']), item['searchnum'])
        item['avgclicknum'] = MathHelper.divide(float(item['clicknum']), item['clickedsearchnum'])
        item['avgclickpos'] = MathHelper.divide(float(item['clickpos']) ,item['clicknum'])
        item['avgdropdown'] = MathHelper.divide(float(item['dropdownnum']), item['searchnum'])
    return result_list