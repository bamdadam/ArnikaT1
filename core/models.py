from django.db import models


# Create your models here.

class FinancialSummary(models.Model):
    PremiumIncome = models.IntegerField()
    OtherIncome = models.IntegerField()
    InvestmentIncome = models.IntegerField()
    Credits = models.IntegerField()
    Expenses = models.IntegerField()
    NetIncome = models.IntegerField()
    Year = models.PositiveIntegerField(unique=True)


# class FinancialPosition(models.Model):
#     CashAndInvestments = models.IntegerField()
#     TotalAssets = models.IntegerField()
#     NetPosition = models.IntegerField()
#     FinancialSummary = models.OneToOneField(FinancialSummary, on_delete=models.CASCADE)
