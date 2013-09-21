# -*- coding: utf-8 -*-

from django.test import TestCase
from kpi.models import CommonQuey
from kpi.models import QueryCategory
from kpi.models import QueryProcess

class OverallTest(TestCase):
    def test_basic_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_get_business(self):
        business_d = CommonQuey().get_business()
        self.assertTrue('主站商户' in business_d)

    def test_get_algo_version(self):
        algo_l = CommonQuey().get_algo_version(3, '2013-09-11', '2013-09-18')
        self.assertTrue(True)

    def test_get_city_list(self):
        city_list = CommonQuey().get_city_list()
        self.assertTrue(len(city_list) > 0)
        
    def test_get_query_type(self):
        query_type = CommonQuey().get_query_type()
        self.assertTrue(len(query_type) > 0)

    def test_get_category(self):
        c_list = CommonQuey().get_category()
        self.assertTrue(len(c_list) > 0)

    def test_get_query_category(self):
        k_list = CommonQuey().get_query_category(3, '2013-09-11', '2013-09-18')
        #self.assertTrue(len(k_list)>0)
        pass

    def test_get_query_process(self):
        k_list = CommonQuey().get_query_process(3, '2013-09-11', '2013-09-18')
        #self.assertTrue(len(k_list)>0)
        pass


class QueryCategoryTest(TestCase):
    """docstring for QueryCategoryTest"""
    def test_to_category_str(self):
        c1 = QueryCategory(1)
        self.assertEqual('name', c1.to_category_str())
        c2 = QueryCategory(4)
        self.assertEqual('chain', c2.to_category_str())
        c3 = QueryCategory(5)
        self.assertEqual('chain+name', c3.to_category_str())


class QueryProcessTest(TestCase):
    """docstring for QueryProcessTest"""
    def test_to_category_str(self):
        q1 = QueryProcess(1)
        self.assertEqual('重定向', q1.to_category_str())
        q2 = QueryProcess(4)
        self.assertEqual('纠错', q2.to_category_str())
        q3 = QueryProcess(5)
        self.assertEqual('纠错+重定向', q3.to_category_str())
        
        