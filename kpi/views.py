from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from kpi.models import CommonQuey
from kpi.models import SeOverallanalysis
from kpi.forms import OverallFilterForm
from django.conf import settings
from django.db.models import Count, Sum, Avg

def index(request):
    context = dict()
    if request.method == 'POST':
        form = OverallFilterForm(request.POST)
        context['message'] = 'to be checked'
        if form.is_valid():
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
            q = q.values('businesstype', 'statdate')
            if algo != None and algo != 'all': 
                q = q.filter(algoversion=algo).values('algoversion')
            if city != None and int(city) != -1: 
                q = q.filter(cityid=city).values('cityid')
            if search_type != None and int(search_type) != -1: 
                q = q.filter(querytype=search_type).values('querytype')
            if category != None and int(category) != -1: 
                q = q.filter(categoryid=category).values('categoryid')
            if query_category != None and int(query_category) != -1: 
                q = q.filter(keywordcategory=query_category).values('keywordcategory')
            if query_process != None and int(query_process) != -1: 
                q = q.filter(searchinfocategory=query_process).values('searchinfocategory')
            q = q.annotate(searchnum=Sum('searchnum'), clicknum=Sum('clicknum'), clickedsearchnum=Sum('clickedsearchnum'))
            print q.query
            for item in q:
                item['clickrate'] = float(item['clickedsearchnum']) / item['searchnum']
            context['overall_result'] = [item for item in q]
    else:
        form = OverallFilterForm()
    context['form'] = form
    return render(request, 'kpi/index.html', context)

def chart(request):
    #member_list = Member.objects.order_by('name')
    context = {}
    return render(request, 'kpi/chart.html', context)
