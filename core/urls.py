from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView

# urls for implemented views
urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view()),
    path('FinancialSummary/<int:Year>/', FinancialSummaryRetrieveUpdateDestroyAPIView.as_view()),
]
