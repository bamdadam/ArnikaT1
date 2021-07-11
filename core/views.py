from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from core.models import FinancialSummary, Company
from core.serializers import FinancialSummarySerializer, CompanySerializer
from core.Mixins import MultipleFieldLookupMixin


# Create your views here.

# basic view for listing all FinancialSummary records
# or creating a FinancialSummary record
class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()


# basic view for Retrieving - Updating - Deleting a specific FinancialSummary record
# which uses the Year field in order to find the specified record
class FinancialSummaryRetrieveUpdateDestroyAPIView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()
    lookup_fields = ['Company', 'Year']


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
