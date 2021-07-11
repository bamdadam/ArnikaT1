from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView

# urls for implemented views
urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view()),
    path('FinancialSummary/<int:Company>/<str:Year>/', FinancialSummaryRetrieveUpdateDestroyAPIView.as_view()),
    path('Company/', CompanyListCreateAPIView.as_view(), )
]
