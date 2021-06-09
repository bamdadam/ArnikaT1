from django.urls import path
from core.views import FinancialSummaryListCreateAPIView

urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view()),
]
