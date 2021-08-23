import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from core.models import FinancialSummary, Company

# Create your tests here.
from core.serializers import FinancialSummarySerializer

client = Client()


class FinancialSummaryTests(TestCase):
    def setUp(self) -> None:
        self.c1 = Company.objects.create(CompanyName="comp1")
        self.c2 = Company.objects.create(CompanyName="comp2")
        self.f1 = FinancialSummary.objects.create(Company=self.c1, NetIncome=2150, Year="2017-02-13")
        self.f2 = FinancialSummary.objects.create(Company=self.c2, NetIncome=2155, Year="2017-04-13")
        self.valid_f1 = {
            # 'Company': self.c2.id,
            'NetIncome': '3100',
            'Year': "2018-11-13"
        }
        self.valid_f2 = {
            'Company': self.c1.id,
            'NetIncome': '25',
            'Year': "2018-11-15"
        }
        self.invalid_f1 = {
            'Company': self.c1.id,
            'NetIncome': "apple",
            'Year': "2018-11-15"
        }

    def test_get_all_FinancialSummary(self):
        response = client.get(reverse('v1:list_create_financial_summary'))
        summaries = FinancialSummary.objects.all()
        serializer = FinancialSummarySerializer(summaries, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_FinancialSummary(self):
        response = client.get(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                      args=[self.c1.id, "2017-02-13"]))
        summary = FinancialSummary.objects.get(Company=self.c1.id, Year="2017-02-13")
        serializer = FinancialSummarySerializer(summary)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_valid_invalid_FinancialSummary(self):
        response = client.patch(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                        args=[self.c1.id, "2017-02-13"]),
                                data=json.dumps(self.valid_f1),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = client.patch(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                        args=[self.c1.id, "2018-11-13"]),
                                data=json.dumps(self.invalid_f1),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_valid_invalid_FinancialSummary(self):
        response = client.post(reverse('v1:list_create_financial_summary'),
                               data=json.dumps(self.valid_f2),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # print(response.data)
        response = client.post(reverse('v1:list_create_financial_summary'),
                               data=json.dumps(self.invalid_f1),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_FinancialSummary(self):
        response = client.delete(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                         args=[self.c2.id, "2017-04-13"]),
                                 content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_update_delete_not_found_FinancialSummary(self):
        response = client.get(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                      args=[self.c1.id, "2017-02-19"]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = client.put(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                      args=[self.c1.id, "2017-02-19"]),
                              data=json.dumps(self.valid_f1),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = client.delete(reverse('v1:retrieve_update_destroy_financial_summary_regular',
                                         args=[self.c2.id, "2017-04-25"]),
                                 content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

