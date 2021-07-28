from django.urls import path, register_converter

from core.converter import PersianPathConverter
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView, \
    CompanyRetrieveUpdateDeleteAPIView

# urls for implemented views
app_name = 'core_app'
register_converter(PersianPathConverter, 'persian_calender')
urlpatterns = [
    path('financialsummary/', FinancialSummaryListCreateAPIView.as_view(),
         name="list_create_financial_summary"),

    path('financialsummary/<int:Company>/<persian_calender:Year>/',
         FinancialSummaryRetrieveUpdateDestroyAPIView.as_view(),
         name="retrieve_update_destroy_financial_summary_persian_date"),

    path('financialsummary/<int:Company>/<str:Year>/',
         FinancialSummaryRetrieveUpdateDestroyAPIView.as_view(),
         name="retrieve_update_destroy_financial_summary_regular"),

    path('financialsummary/<int:NetIncome>/',
         FinancialSummaryListCreateAPIView.as_view(),
         name="list_financial_summary_net_income"),

    path('company/', CompanyListCreateAPIView.as_view(),
         name="list_create_company"),

    path('company/<int:pk>/', CompanyRetrieveUpdateDeleteAPIView.as_view(),
         name="retrieve_update_destroy_company"),
]
