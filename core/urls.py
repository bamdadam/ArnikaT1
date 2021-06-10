from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, FinancialSummaryRetrieveAPIView

urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view()),
    path('FinancialSummary/<int:Year>/', FinancialSummaryRetrieveAPIView.as_view()),
]
