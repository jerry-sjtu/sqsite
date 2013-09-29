from django import forms
from kpi.models import CommonQuey
from kpi.forms import SimpleChoiceFeild
import datetime

class HotqueryFilterForm(forms.Form):
    q = CommonQuey()
    city_list = forms.ChoiceField(q.get_city_list()) 

    def __init__(self, *args, **kwargs):
        q = CommonQuey()
        business = kwargs.pop('business', 1)
        fromdate = kwargs.pop('fromdate', datetime.datetime.now)
        todate = kwargs.pop('todate', datetime.datetime.now)
        #the pop statements should be executed first
        super(HotqueryFilterForm, self).__init__(*args, **kwargs)
        self.fields['business'] = forms.ChoiceField(q.get_business(), initial=business)
        self.fields['fromdate'] = forms.DateField(initial=fromdate)
        self.fields['todate'] = forms.DateField(initial=todate)
        self.fields['algo_list'] = SimpleChoiceFeild(q.get_algo_version(business, fromdate, todate))