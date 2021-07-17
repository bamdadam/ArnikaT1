from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException, NotFound
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

# from core.exceptions import PageNotFound
from core.exceptions import PageNotFound
from core.models import FinancialSummary, Company
from core.serializers import FinancialSummarySerializer, CompanySerializer
from core.Mixins import MultipleFieldLookupMixin


# Create your views here.

# basic view for listing all FinancialSummary records
# or creating a FinancialSummary record
class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FinancialSummarySerializer

    def get_queryset(self):
        net_income = self.kwargs.get('NetIncome')
        if net_income:
            queryset = FinancialSummary.objects.filter(NetIncome=net_income)
        else:
            queryset = FinancialSummary.objects.all()
        return queryset


# basic view for Retrieving - Updating - Deleting a specific FinancialSummary record
# which uses the Year field in order to find the specified record
class FinancialSummaryRetrieveUpdateDestroyAPIView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()
    lookup_fields = ['Company', 'Year']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'done'}, status=status.HTTP_204_NO_CONTENT)


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class CompanyRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'done'}, status=status.HTTP_204_NO_CONTENT)


@api_view()
def error_page(request, exception):
    raise PageNotFound
