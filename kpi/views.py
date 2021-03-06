from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from kpi.models import CommonQuey, FormatHelper, MathHelper, str_to_date, SeOverallanalysis
from kpi.forms import OverallFilterForm, SimpleChoiceFeild
from django import forms
from django.conf import settings
from django.db.models import Count, Sum, Avg
import json
import datetime

def index(request):
    context = dict()
    if request.method == 'POST':
        form = OverallFilterForm(request.POST)
        request.POST['algo_list'] 
        if form.is_valid():
            #there wll be cleaned data after validated
            result_list = overall_query(form, False)
            total_list = overall_query(form, True)
            business = form.cleaned_data['business']
            fromdate = form.cleaned_data['fromdate']
            todate = form.cleaned_data['todate']
            form = OverallFilterForm(request.POST, business=business, fromdate=fromdate, todate=todate)
            context['overall_result'] = result_list
            context['total_result'] = total_list
    else:
        form = OverallFilterForm(business=1, fromdate=datetime.datetime.now, todate=datetime.datetime.now)
    context['form'] = form
    return render(request, 'kpi/index.html', context)

@cache_page(60 * 60 * 24)
def algo_list(request, business, fromdate, todate):
    fromdate = str_to_date(fromdate)
    todate = str_to_date(todate)
    algo_list = CommonQuey().get_algo_version(business, fromdate, todate)
    return HttpResponse(json.dumps(algo_list), content_type="application/json")

@cache_page(60 * 60 * 24)
def query_category(request, business, fromdate, todate):
    fromdate = str_to_date(fromdate)
    todate = str_to_date(todate)
    query_category_list = CommonQuey().get_query_category(business, fromdate, todate)
    return HttpResponse(json.dumps(query_category_list), content_type="application/json")

def chart(request):
    context = dict()
    return render(request, 'kpi/chart.html', context)

def overall_query(form, is_single):
    business = form.cleaned_data['business']
    fromdate = form.cleaned_data['fromdate']
    todate = form.cleaned_data['todate']
    algo = form.cleaned_data['algo_list']
    city = form.cleaned_data['city_list']
    search_type = form.cleaned_data['search_type']
    category = form.cleaned_data['category_list']
    query_category = form.cleaned_data['query_category']
    query_process = form.cleaned_data['query_process']

    q = SeOverallanalysis.objects.filter(businesstype=business,statdate__gte=fromdate,statdate__lte=todate)
    if is_single == False:  
        q = q.values('businesstype', 'statdate')
    else:
        q = q.values('businesstype')
    if algo != None and algo != 'all': 
        q = q.filter(algoversion=algo)
    if city != None and int(city) != -1: 
        q = q.filter(cityid=city)
    if search_type != None and int(search_type) != -1: 
        q = q.filter(querytype=search_type)
    if category != None and int(category) != -1: 
        q = q.filter(categoryid=category)
    if query_category != None and int(query_category) != -1: 
        q = q.filter(keywordcategory=query_category)
    if query_process != None and int(query_process) != -1: 
        q = q.filter(searchinfocategory=query_process)
    q = q.annotate(searchnum=Sum('searchnum'), clicknum=Sum('clicknum'), clickedsearchnum=Sum('clickedsearchnum'),
        clickpos=Sum('clickpos'), firstclickpos=Sum('firstclickpos'), pageoneclickedsearchnum=Sum('pageoneclickedsearchnum'),
        pageoneclicknum=Sum('pageoneclicknum'), pageoneclickpos=Sum('pageoneclickpos'), hotkeywordsearchnum=Sum('hotkeywordsearchnum'),
        hotkeywordclickedsearchnum=Sum('hotkeywordclickedsearchnum'), dropdownnum=Sum('dropdownnum'),noresultnum=Sum('noresultnum'))
    if is_single == False:
        q = q.order_by('-statdate',)
        #print q.query
    q = fill_ratio(q)
    return fill_date_info(q, fromdate, todate)

def fill_date_info(result_list, from_date, to_date):
    for item in result_list:
        item['from_date']  = from_date
        item['to_date'] = to_date
    return result_list

def fill_ratio(result_list):
    for item in result_list:
        item['clickrate'] = MathHelper.divide(float(item['clickedsearchnum']), item['searchnum'])
        item['avgclicknum'] = MathHelper.divide(float(item['clicknum']), item['clickedsearchnum'])
        item['avgclickpos'] = MathHelper.divide(float(item['clickpos']) ,item['clicknum'])
        item['avgfirstclickpos'] = MathHelper.divide(float(item['firstclickpos']), item['clickedsearchnum'])
        item['avgpageoneclicknum'] = MathHelper.divide(float(item['pageoneclicknum']), item['pageoneclickedsearchnum'])
        item['avgpageoneclickpos'] = MathHelper.divide(float(item['pageoneclickpos']), item['pageoneclicknum'])
        item['hotclickrate'] = MathHelper.divide(float(item['hotkeywordclickedsearchnum']) ,item['hotkeywordsearchnum'])
        item['avgdropdown'] = MathHelper.divide(float(item['dropdownnum']), item['searchnum'])
        item['noresultrate'] = MathHelper.divide(float(item['noresultnum']),item['searchnum'])
    return result_list

