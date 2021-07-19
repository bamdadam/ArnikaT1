import traceback
from datetime import datetime
from rest_framework import serializers
from core.models import FinancialSummary, Company


# simple Serializer class for FinancialSummary model
# for now it takes all the fields and just Serializes them
class FinancialSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialSummary
        fields = ['NetIncome', 'Year', 'Company']

    def validate_Year(self, value):
        if value > datetime.now().date():
            raise serializers.ValidationError("Please enter a valid Date")
        return value


class CompanySerializer(serializers.ModelSerializer):
    financialsummary = FinancialSummarySerializer(required=False, many=True, read_only=True)

    class Meta:
        model = Company
        fields = ['CompanyName', 'financialsummary', 'id']

    def create(self, validated_data):
        try:
            company = Company.objects.create(**validated_data)
        except TypeError:
            tb = traceback.format_exc()
            raise TypeError(tb)
        return company
