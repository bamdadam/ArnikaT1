from rest_framework import serializers
from core.models import FinancialSummary, FinancialPosition


class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialSummary
        fields = ('PremiumIncome', 'OtherIncome', 'InvestmentIncome',
                  'Credits', 'Expenses', 'NetIncome', 'Year', 'id')
