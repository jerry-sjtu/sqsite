# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
import os
import datetime
from django.db.models import Count, Sum

def str_to_date(str):
    try:
        year,month,day = str.strip().split('-')
        return datetime.date(int(year), int(month), int(day))
    except:
        return datetime.date.today()

class SeOverallanalysis(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID') # Field name made lowercase.
    querytype = models.IntegerField(db_column='QueryType') # Field name made lowercase.
    businesstype = models.IntegerField(db_column='BusinessType') # Field name made lowercase.
    algoversion = models.CharField(max_length=50L, db_column='AlgoVersion') # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID') # Field name made lowercase.
    searchinfocategory = models.IntegerField(null=True, db_column='SearchInfoCategory', blank=True) # Field name made lowercase.
    keywordcategory = models.IntegerField(null=True, db_column='KeywordCategory', blank=True) # Field name made lowercase.
    hasad = models.IntegerField(null=True, db_column='HasAd', blank=True) # Field name made lowercase.
    statdate = models.DateField(db_column='StatDate') # Field name made lowercase.
    searchnum = models.IntegerField(db_column='SearchNum') # Field name made lowercase.
    clickedsearchnum = models.IntegerField(db_column='ClickedSearchNum') # Field name made lowercase.
    clicknum = models.IntegerField(db_column='ClickNum') # Field name made lowercase.
    clickpos = models.IntegerField(db_column='ClickPos') # Field name made lowercase.
    pageoneclickedsearchnum = models.IntegerField(db_column='PageOneClickedSearchNum') # Field name made lowercase.
    pageoneclicknum = models.IntegerField(db_column='PageOneClickNum') # Field name made lowercase.
    pageoneclickpos = models.IntegerField(db_column='PageOneClickPos') # Field name made lowercase.
    hotkeywordsearchnum = models.IntegerField(db_column='HotKeywordSearchNum') # Field name made lowercase.
    hotkeywordclickedsearchnum = models.IntegerField(db_column='HotKeywordClickedSearchNum') # Field name made lowercase.
    noresultnum = models.IntegerField(db_column='NoResultNum') # Field name made lowercase.
    totalwordnum = models.IntegerField(db_column='TotalWordNum') # Field name made lowercase.
    noclickwordnum = models.IntegerField(db_column='NoClickWordNum') # Field name made lowercase.
    noresultwordnum = models.IntegerField(db_column='NoResultWordNum') # Field name made lowercase.
    dropdownnum = models.IntegerField(db_column='DropDownNum') # Field name made lowercase.
    firstclickpos = models.IntegerField(db_column='FirstClickPos') # Field name made lowercase.
    adnum = models.IntegerField(null=True, db_column='AdNum', blank=True) # Field name made lowercase.
    clickedsearchnum_noad = models.IntegerField(null=True, db_column='ClickedSearchNum_NoAd', blank=True) # Field name made lowercase.
    clicknum_noad = models.IntegerField(null=True, db_column='ClickNum_NoAd', blank=True) # Field name made lowercase.
    clickpos_noad = models.IntegerField(null=True, db_column='ClickPos_NoAd', blank=True) # Field name made lowercase.
    tuangouinfonum = models.IntegerField(null=True, db_column='TuangouInfoNum', blank=True) # Field name made lowercase.
    tuangoubuynum = models.IntegerField(null=True, db_column='TuangouBuyNum', blank=True) # Field name made lowercase.
    tuangousubmitnum = models.IntegerField(null=True, db_column='TuangouSubmitNum', blank=True) # Field name made lowercase.
    bookinginfonum = models.IntegerField(null=True, db_column='BookingInfoNum', blank=True) # Field name made lowercase.
    bookingsubmitnum = models.IntegerField(null=True, db_column='BookingSubmitNum', blank=True) # Field name made lowercase.
    cardinfonum = models.IntegerField(null=True, db_column='CardInfoNum', blank=True) # Field name made lowercase.
    cardjoinnum = models.IntegerField(null=True, db_column='CardJoinNum', blank=True) # Field name made lowercase.
    couponinfonum = models.IntegerField(null=True, db_column='CouponInfoNum', blank=True) # Field name made lowercase.
    coupondownloadnum = models.IntegerField(null=True, db_column='CouponDownloadNum', blank=True) # Field name made lowercase.

    class Meta:
        db_table = 'SE_OverallAnalysis'

    def __unicode__(self):
        return self.name

    def get_business(self):
        pass

class FormatHelper(object):
    @staticmethod
    def format_float(val):
        return '{0:.3f}'.format(val)

class MathHelper(object):
    @staticmethod
    def divide(num1, num2):
        if num2 == 0:
            return 0
        else:
            return '{0:.3f}'.format(float(num1) / num2)
        
        

class CommonQuey(models.Model):
    def __init__(self):
        self.init_city()

    def get_business(self):
        return settings.KPI_CONF['business']

    def get_query_type(self):
        return settings.KPI_CONF['query_type']

    def get_category(self):
        return settings.KPI_CONF['category']

    def get_query_category(self, business, start_date, to_date):
        '''query understanding'''
        start_date = str_to_date(start_date)
        to_date = str_to_date(to_date)
        q = SeOverallanalysis.objects.filter(statdate__gte=start_date,statdate__lte=to_date, businesstype=business) \
            .values('keywordcategory').annotate(search_num=Sum('searchnum')).order_by('-search_num')[:20]
        #print q.query
        re =[QueryCategory(item['keywordcategory']) for item in q]
        return [(-1, 'all')] + [(item.mask, item.to_category_str()) for item in re]

    def get_query_process(self, business, start_date, to_date):
        start_date = str_to_date(start_date)
        to_date = str_to_date(to_date)
        q = SeOverallanalysis.objects.filter(statdate__gte=start_date,statdate__lte=to_date, businesstype=business) \
            .values('searchinfocategory').distinct()
        #print q.query
        re = [QueryProcess(item['searchinfocategory']) for item in q]
        return [(-1, 'all')] + [(item.mask, item.to_category_str()) for item in re]

    def parse_stat_time(self, stat_time):
        today = datetime.date.today()
        if stat_time == 'yesterday':
            yesterday = today - datetime.timedelta(days=1)
            return yesterday.strftime('%Y-%m-%d') 
        elif stat_time == 'today':
            return today.strftime('%Y-%m-%d') 

    def get_algo_version(self, business, start_date, to_date):
        start_date = str_to_date(start_date)
        to_date = str_to_date(to_date)
        q = SeOverallanalysis.objects.filter(statdate__gte=start_date,statdate__lte=to_date, businesstype=business) \
            .values('algoversion').distinct()
        algo_list = [('all', 'all')]
        return algo_list + [(item['algoversion'],item['algoversion']) for item in q]

    def get_city_list(self):
        return self.city_l

    def init_city(self):
        self.city_d = dict()
        self.city_l = list()
        for line in open(os.path.join(settings.BASE_DIR, "static/resource/cityname")):
            city, id = line.strip().split(',')
            self.city_d[city] = id
            self.city_l.append((id, city))

class QueryCategory(object):
    """docstring for QueryCategory"""
    def __init__(self, mask):
        super(QueryCategory, self).__init__()
        self.index_d = self.init_index_map()
        self.mask = mask

    def init_index_map(self):
        index_d = dict()
        index_d[0] = "name"
        index_d[1] = "brand"
        index_d[2] = "chain"
        index_d[3] = "squareCenterLandmark"
        index_d[4] = "address"
        index_d[5] = "cross"
        index_d[6] = "region"
        index_d[7] = "busword"
        index_d[8] = "dishTag"
        index_d[9] = "shopTag"
        index_d[10] = "tag"
        index_d[11] = "leafCat"
        index_d[12] = "inCat"
        return index_d
        
    def to_category_str(self):
        bit_str =  "{0:b}".format(self.mask)
        category_l = list()
        for i in range(0, len(bit_str)):
            j = len(bit_str) - 1 - i
            c = bit_str[i]
            if c == '1': category_l.append(self.index_d[j])
        if len(category_l) == 0:
            return "other"
        return '+'.join(category_l)
        
class QueryProcess(object):
    """docstring for QueryProcess"""
    def __init__(self, mask):
        self.index_d = self.init_index_map()
        self.mask = mask

    def to_category_str(self):
        bit_str =  "{0:b}".format(self.mask)
        category_l = list()
        for i in range(0, len(bit_str)):
            j = len(bit_str) - 1 - i
            c = bit_str[i]
            if c == '1': category_l.append(self.index_d[j])
        if len(category_l) == 0:
            return "other"
        return '+'.join(category_l)
        
    def init_index_map(self):
        index_d = dict()
        index_d[0] = "重定向"
        index_d[1] = "个性化"
        index_d[2] = "纠错"
        return index_d
