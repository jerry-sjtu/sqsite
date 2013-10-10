# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class SeCheatkeyword(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    adddate = models.DateField(db_column='AddDate') # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID') # Field name made lowercase.
    businesstype = models.IntegerField(db_column='BusinessType') # Field name made lowercase.
    keyword = models.CharField(max_length=50L, db_column='Keyword') # Field name made lowercase.
    searchnum = models.IntegerField(db_column='SearchNum') # Field name made lowercase.
    clickedsearchnum = models.IntegerField(db_column='ClickedSearchNum') # Field name made lowercase.
    crosscitynum = models.IntegerField(db_column='CrossCityNum') # Field name made lowercase.
    hitnum = models.IntegerField(db_column='HitNum') # Field name made lowercase.
    ischeat = models.IntegerField(db_column='IsCheat') # Field name made lowercase.
    class Meta:
        db_table = 'SE_CheatKeyword'

class SeOverallanalysis(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
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

class SeQueryanalysis(models.Model):
    id = models.IntegerField(db_column='ID') # Field name made lowercase.
    businesstype = models.IntegerField(db_column='BusinessType') # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID') # Field name made lowercase.
    regionid = models.IntegerField(db_column='RegionID') # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryID') # Field name made lowercase.
    algoversion = models.CharField(max_length=50L, db_column='AlgoVersion') # Field name made lowercase.
    statdate = models.DateField(db_column='StatDate') # Field name made lowercase.
    keyword = models.CharField(max_length=64L, db_column='Keyword') # Field name made lowercase.
    keywordtype = models.IntegerField(db_column='KeywordType') # Field name made lowercase.
    searchnum = models.IntegerField(db_column='SearchNum') # Field name made lowercase.
    clickedsearchnum = models.IntegerField(db_column='ClickedSearchNum') # Field name made lowercase.
    clicknum = models.IntegerField(db_column='ClickNum') # Field name made lowercase.
    clickpos = models.IntegerField(db_column='ClickPos') # Field name made lowercase.
    dropdownnum = models.IntegerField(db_column='DropDownNum') # Field name made lowercase.
    resultnum = models.IntegerField(null=True, db_column='ResultNum', blank=True) # Field name made lowercase.
    addtag2 = models.DecimalField(decimal_places=2, null=True, max_digits=6, db_column='AddTag2', blank=True) # Field name made lowercase.
    addtag3 = models.DecimalField(decimal_places=2, null=True, max_digits=6, db_column='AddTag3', blank=True) # Field name made lowercase.
    addtag4 = models.DecimalField(decimal_places=2, null=True, max_digits=6, db_column='AddTag4', blank=True) # Field name made lowercase.
    class Meta:
        db_table = 'SE_QueryAnalysis'

