from django.shortcuts import render
from rest_framework import generics
from core.models import FinancialPosition, FinancialSummary
from core.serializers import FinancialSummarySerializer


# Create your views here.


class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()
