import traceback
from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from rest_framework import serializers
from core.models import FinancialSummary, Company


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'company_admin']
        read_only_fields = ['company_admin']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()
        return user


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

    def update(self, instance, validated_data):
        if 'Company' in validated_data:
            raise serializers.ValidationError(
                {
                    'Company': "Can't Change The Company Field After Financial Summary Creation"
                }
            )
        return super(FinancialSummarySerializer, self).update(instance, validated_data)


class CompanySerializer(serializers.ModelSerializer):
    financialsummary = FinancialSummarySerializer(required=False, many=True, read_only=True)
    admins = UserSerializer(required=False, many=True, )

    class Meta:
        model = Company
        fields = ['CompanyName', 'financialsummary', 'admins', 'id']

    def create(self, validated_data):
        try:
            company = super(CompanySerializer, self).create(validated_data)
            company.admins.add(self.context["request"].user)
        except TypeError:
            tb = traceback.format_exc()
            raise TypeError(tb)
        return company


class AddAdminToCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['admins', 'id']

    def update(self, instance, validated_data):
        if 'id' in validated_data:
            raise serializers.ValidationError(
                {
                    'id': "Can't Change Company id After Creation"
                }
            )
        instance.admins.add(*[user.id for user in validated_data['admins']])
        return instance


class DeleteAdminToCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['admins', 'id']

    def update(self, instance, validated_data):
        if 'id' in validated_data:
            raise serializers.ValidationError(
                {
                    'id': "Can't Change Company id After Creation"
                }
            )
        instance.admins.remove(*[user.id for user in validated_data['admins']])
        return instance
