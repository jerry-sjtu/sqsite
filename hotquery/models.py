from django.db import models
import datetime


class SeQueryanalysis(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True) # Field name made lowercase.
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
