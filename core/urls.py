from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView, \
    CompanyRetrieveUpdateDeleteAPIView

# urls for implemented views
app_name = 'core_app'
urlpatterns = [
    path('FinancialSummary/', FinancialSummaryListCreateAPIView.as_view(),),
    path('FinancialSummary/<int:Company>/<str:Year>/', FinancialSummaryRetrieveUpdateDestroyAPIView.as_view()),
    path('FinancialSummary/<int:NetIncome>/', FinancialSummaryListCreateAPIView.as_view()),
    path('Company/', CompanyListCreateAPIView.as_view(), ),
    path('Company/<int:pk>/', CompanyRetrieveUpdateDeleteAPIView.as_view(),),
]

