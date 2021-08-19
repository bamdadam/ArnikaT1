from core.serializers import FinancialSummarySerializer, CompanySerializer, \
    UserSerializer, AddAdminToCompanySerializer, DeleteAdminToCompanySerializer

FinancialSummarySerializer_dict = {
    'v1': FinancialSummarySerializer
}

CompanySerializer_dict = {
    'v1': CompanySerializer
}

UserSerializer_dict = {
    'v1': UserSerializer
}

AddAdminToCompany_dict = {
    'v1': AddAdminToCompanySerializer
}

DeleteAdminToCompany_dict = {
    'v1': DeleteAdminToCompanySerializer
}
