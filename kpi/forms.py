from django import forms
from kpi.models import CommonQuey
import datetime
from django.core.exceptions import ValidationError


class SimpleChoiceFeild(forms.ChoiceField):

    #the content of the field may be changed by the ajax,
    #so the check should be skipped.
    def validate(self, value):
        if value == None:
            raise ValidationError(u'filed is of null value')

class OverallFilterForm(forms.Form):
    q = CommonQuey()
    city_list = forms.ChoiceField(q.get_city_list()) 
    search_type = forms.ChoiceField(q.get_query_type()) 
    category_list = forms.ChoiceField(q.get_category()) 

    def __init__(self, *args, **kwargs):
        q = CommonQuey()
        business = kwargs.pop('business', 1)
        fromdate = kwargs.pop('fromdate', datetime.datetime.now)
        todate = kwargs.pop('todate', datetime.datetime.now)
        #the pop statements should be executed first
        super(OverallFilterForm, self).__init__(*args, **kwargs)
        self.fields['business'] = forms.ChoiceField(q.get_business(), initial=business)
        self.fields['fromdate'] = forms.DateField(initial=fromdate)
        self.fields['todate'] = forms.DateField(initial=todate)
        self.fields['algo_list'] = SimpleChoiceFeild(q.get_algo_version(business, fromdate, todate))
        self.fields['query_category'] = SimpleChoiceFeild(q.get_query_category(business, fromdate, todate))
        self.fields['query_process'] = SimpleChoiceFeild(q.get_query_process(business, fromdate, todate)) 


