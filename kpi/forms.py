from django import forms
from kpi.models import CommonQuey


class OverallFilterForm(forms.Form):
    q = CommonQuey()
    init_business = 3
    init_fromdate = '2013-09-10'
    init_todate = '2013-09-18'
    business = forms.ChoiceField(q.get_business())
    fromdate = forms.DateField()
    todate = forms.DateField()
    algo_list = forms.ChoiceField(q.get_algo_version(init_business, init_fromdate, init_todate))
    city_list = forms.ChoiceField(q.get_city_list()) 
    search_type = forms.ChoiceField(q.get_query_type()) 
    category_list = forms.ChoiceField(q.get_category()) 
    query_category = forms.ChoiceField(q.get_query_category(init_business, init_fromdate, init_todate)) 
    query_process = forms.ChoiceField(q.get_query_process(init_business, init_fromdate, init_todate)) 