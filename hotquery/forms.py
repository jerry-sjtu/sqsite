from django import forms
from kpi.models import CommonQuey
import datetime

class HotqueryFilterForm(forms.Form):
    q = CommonQuey()
    business = forms.ChoiceField(q.get_business(), initial='1')
    fromdate = forms.DateField(initial=datetime.datetime.now)
    todate = forms.DateField(initial=datetime.datetime.now)
    algo_list = forms.ChoiceField(initial=q.get_algo_version(1, datetime.datetime.now, datetime.datetime.now))
    city_list = forms.ChoiceField(q.get_city_list()) 