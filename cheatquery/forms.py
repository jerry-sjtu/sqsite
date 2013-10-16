from django import forms
from kpi.models import CommonQuey
import datetime

class CheatQueryFilterForm(forms.Form):
    q = CommonQuey()
    city_list = forms.ChoiceField(q.get_city_list()) 

    def __init__(self, *args, **kwargs):
        q = CommonQuey()
        business = kwargs.pop('business', 1)
        fromdate = kwargs.pop('fromdate', datetime.datetime.now)
        todate = kwargs.pop('todate', datetime.datetime.now)
        #the pop statements should be executed first
        super(CheatQueryFilterForm, self).__init__(*args, **kwargs)
        self.fields['business'] = forms.ChoiceField(q.get_business(), initial=business)
        self.fields['fromdate'] = forms.DateField(initial=fromdate)
        self.fields['todate'] = forms.DateField(initial=todate)
