from django.db import models


# Create your models here.
# simple Financial model based of Financial data highlighted from PBGC's financial statements
# for the periods ending September 30, 1992 through September 30, 2009.
# https://data.world/finance/pbgc-financial-summary-data
# at the moment we dont have any particular data dependency between tables
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
