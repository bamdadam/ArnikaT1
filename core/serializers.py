import traceback
from datetime import datetime, date

from rest_framework import serializers
from core.models import FinancialSummary, Company


# simple Serializer class for FinancialSummary model
# for now it takes all the fields and just Serializes them
class FinancialSummarySerializer(serializers.ModelSerializer):
    # print(validated_data)

    class Meta:
        model = FinancialSummary
        fields = ['NetIncome', 'Year']

    def validate_Year(self, value):
        try:
            # print(value)
            # date = datetime.strptime(value, '%Y-%m-%d')
            if value > datetime.now().date():
                raise serializers.ValidationError("Please enter a valid Date")
        except ValueError:
            raise serializers.ValidationError("Incorrect data format, should be YYYY-MM-DD")


class CompanySerializer(serializers.ModelSerializer):
    financialsummary = FinancialSummarySerializer(many=True, )

    class Meta:
        model = Company
        fields = ['CompanyName', 'financialsummary', 'id']

    def create(self, validated_data):
        finances_data = validated_data.pop('financialsummary')
        try:
            company = Company.objects.create(**validated_data)
            for finance_data in finances_data:
                try:
                    print(finance_data)
                    FinancialSummary.objects.create(Company=company, **finance_data)
                except TypeError:
                    tb = traceback.format_exc()
                    raise TypeError(tb)
        except TypeError:
            tb = traceback.format_exc()
            # print(tb)
            raise TypeError(tb)
        return company
