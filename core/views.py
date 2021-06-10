from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from core.models import FinancialPosition, FinancialSummary
from core.serializers import FinancialSummarySerializer


# Create your views here.


class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()


class FinancialSummaryRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = FinancialSummarySerializer
    queryset = FinancialSummary.objects.all()
    lookup_field = 'Year'
    lookup_url_kwarg = 'Year'

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
    #     assert lookup_url_kwarg in self.kwargs, (
    #         (self.__class__.__name__, lookup_url_kwarg)
    #     )
    #     filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
    #     obj = get_object_or_404(queryset, **filter_kwargs)
    #     self.check_object_permissions(self.request, obj)
    #     return obj
