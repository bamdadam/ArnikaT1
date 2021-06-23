from rest_framework import serializers
from core.models import FinancialSummary

# simple Serializer class for FinancialSummary model
# for now it takes all the fields and just Serializes them
class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialSummary
        fields = ('PremiumIncome', 'OtherIncome', 'InvestmentIncome',
                  'Credits', 'Expenses', 'NetIncome', 'Year', 'id')
