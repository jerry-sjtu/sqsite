from django.db import models
from django.conf import settings

class SeCheatkeyword(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    adddate = models.DateField(db_column='AddDate') # Field name made lowercase.
    cityid = models.IntegerField(db_column='CityID') # Field name made lowercase.
    business = models.IntegerField(db_column='BusinessType') # Field name made lowercase.
    keyword = models.CharField(max_length=50L, db_column='Keyword') # Field name made lowercase.
    searchnum = models.IntegerField(db_column='SearchNum') # Field name made lowercase.
    clickedsearchnum = models.IntegerField(db_column='ClickedSearchNum') # Field name made lowercase.
    crosscitynum = models.IntegerField(db_column='CrossCityNum') # Field name made lowercase.
    hitnum = models.IntegerField(db_column='HitNum') # Field name made lowercase.
    ischeat = models.IntegerField(db_column='IsCheat') # Field name made lowercase.
    class Meta:
        db_table = 'SE_CheatKeyword'


class CommonQuery(object):
    def __init__(self, arg):
        super(CommonQuery, self).__init__()
        self.city_list = parse_city_list()

    def get_city_list(self):
        return self.city_list
    
    @staticmethod
    def parse_city_list():
        for line in open(os.path.join(settings.BASE_DIR, "static/resource/cityname")):
            city, id = line.strip().split(',')
            self.city_l.append((id, city))
