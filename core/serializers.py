from rest_framework import serializers
from core.models import FinancialSummary, Company


# simple Serializer class for FinancialSummary model
# for now it takes all the fields and just Serializes them
class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialSummary
        fields = ['NetIncome', 'Year']


class CompanySerializer(serializers.ModelSerializer):
    financialsummary = FinancialSummarySerializer(many=True,)

    class Meta:
        model = Company
        fields = ['CompanyName', 'financialsummary']

    def create(self, validated_data):
        print(validated_data)
        finances_data = validated_data.pop('financialsummary')
        company = Company.objects.create(**validated_data)
        for finance_data in finances_data:
            FinancialSummary.objects.create(Company=company, **finance_data)

        return company
