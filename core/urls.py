from django.urls import path
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView, \
    CompanyRetrieveUpdateDeleteAPIView

# urls for implemented views
app_name = 'core_app'
urlpatterns = [
    path('financialsummary/', FinancialSummaryListCreateAPIView.as_view(),),
    path('financialsummary/<int:Company>/<str:Year>/', FinancialSummaryRetrieveUpdateDestroyAPIView.as_view()),
    path('financialsummary/<int:NetIncome>/', FinancialSummaryListCreateAPIView.as_view()),
    path('company/', CompanyListCreateAPIView.as_view(), ),
    path('company/<int:pk>/', CompanyRetrieveUpdateDeleteAPIView.as_view(),),
]

