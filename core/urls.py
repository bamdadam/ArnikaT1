from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view()),
    path('FinancialSummary/<int:Year>/', FinancialSummaryRetrieveUpdateDestroyAPIView.as_view()),
]
