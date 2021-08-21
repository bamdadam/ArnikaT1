from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics, status, mixins
from rest_framework.decorators import api_view
from rest_framework.exceptions import APIException, NotFound
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from core.exceptions import PageNotFound
from core.Version_dicts import FinancialSummarySerializer_dict, CompanySerializer_dict, UserSerializer_dict, \
    AddAdminToCompany_dict, DeleteAdminToCompany_dict
from core.exceptions import PageNotFound, WrongDataFormat, ObjectNotExist
from core.models import FinancialSummary, Company
from core.permissions import IsCompanyAdmin
from core.serializers import FinancialSummarySerializer, CompanySerializer, UserSerializer, AddAdminToCompanySerializer, \
    DeleteAdminToCompanySerializer
from core.Mixins import MultipleFieldLookupMixin


# Create your views here.

# basic view for listing all FinancialSummary records
# or creating a FinancialSummary record
class FinancialSummaryListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsCompanyAdmin)

    def get_queryset(self):
        net_income = self.kwargs.get('NetIncome')
        if net_income:
            queryset = FinancialSummary.objects.filter(NetIncome=net_income)
        else:
            queryset = FinancialSummary.objects.all()
        return queryset

    def get_serializer_class(self):
        return FinancialSummarySerializer_dict.get(self.request.version, FinancialSummarySerializer)


# basic view for Retrieving - Updating - Deleting a specific FinancialSummary record
# which uses the Year field in order to find the specified record
class FinancialSummaryRetrieveUpdateDestroyAPIView(MultipleFieldLookupMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsCompanyAdmin)
    queryset = FinancialSummary.objects.all()
    lookup_fields = ['Company', 'Year']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'done'}, status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return FinancialSummarySerializer_dict.get(self.request.version, FinancialSummarySerializer)


class CompanyListCreateAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return CompanySerializer_dict.get(self.request.version, CompanySerializer)


class CompanyRetrieveUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated, IsCompanyAdmin)
    lookup_url_kwarg = 'Company'

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'detail': 'done'}, status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return CompanySerializer_dict.get(self.request.version, CompanySerializer)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )
        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        if not hasattr(queryset, 'get'):
            queryset__name = queryset.__name__ if isinstance(queryset, type) else queryset.__class__.__name__
            raise ValueError(
                "First argument to get_object_or_404() must be a Model, Manager, "
                "or QuerySet, not '%s'." % queryset__name
            )
        try:
            obj = queryset.get(**filter_kwargs)
        except queryset.model.DoesNotExist:
            model_instance = queryset.model.__name__
            # raise Http404('No %s matches the given query.' % queryset.model._meta.object_name)
            raise PageNotFound(detail=f"No {model_instance} matches the given query.")
        self.check_object_permissions(self.request, obj)
        return obj


class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        return UserSerializer_dict.get(self.request.version, UserSerializer)


class AddDeleteAdminToCompany(mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    queryset = Company.objects.all()
    permission_classes = (IsAuthenticated, IsCompanyAdmin)
    lookup_url_kwarg = 'Company'

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return AddAdminToCompany_dict.get(self.request.version, AddAdminToCompanySerializer)
        elif self.request.method == 'DELETE':
            return DeleteAdminToCompany_dict.get(self.request.version, DeleteAdminToCompanySerializer)

    def delete(self, request, *args, **kwargs):
        return super(AddDeleteAdminToCompany, self).update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super(AddDeleteAdminToCompany, self).update(request, *args, **kwargs)


@api_view()
def error_page(request, exception):
    raise PageNotFound
