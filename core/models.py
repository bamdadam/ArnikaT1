from django.db import models


# Create your models here.

class FinancialSummary(models.Model):
    PremiumIncome = models.IntegerField
    OtherIncome = models.IntegerField
    InvestmentIncome = models.IntegerField
    Credits = models.IntegerField
    Expenses = models.IntegerField
    NetIncome = models.IntegerField
    Year = models.PositiveIntegerField


class FinancialPosition(models.Model):
    CashAndInvestments = models.IntegerField
    TotalAssets = models.IntegerField
