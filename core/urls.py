from django.urls import path, register_converter
from rest_framework import routers

from core.converter import PersianPathConverter
from core.views import FinancialSummaryListCreateAPIView, \
    FinancialSummaryRetrieveUpdateDestroyAPIView, CompanyListCreateAPIView, \
    CompanyRetrieveUpdateDeleteAPIView, UserListCreateAPIView, AddAdminToCompany, DeleteAdminToCompany
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urls for implemented views
app_name = 'core_app'
register_converter(PersianPathConverter, 'persian_calender')
# router = routers.SimpleRouter()
# router.register(r'company', )
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('refresh-token/', TokenRefreshView.as_view(), name='token_refresh'),

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

    path('company/<int:pk>/addadmin/', AddAdminToCompany.as_view(),
         name="add_admin_for_company"),

    path('company/<int:pk>/deleteadmin/', DeleteAdminToCompany.as_view(),
         name="delete_admin_for_company"),

    path('registeruser/', UserListCreateAPIView.as_view(),
         name='register_user'),

]
