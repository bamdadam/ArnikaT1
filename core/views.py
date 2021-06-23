from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from core.models import FinancialSummary
from core.serializers import FinancialSummarySerializer


# Create your views here.

# basic view for listing all FinancialSummary records
# or creating a FinancialSummary record
class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()


# basic view for Retrieving - Updating - Deleting a specific FinancialSummary record
# which uses the Year field in order to find the specified record
class FinancialSummaryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()
    lookup_field = 'Year'
    lookup_url_kwarg = 'Year'
