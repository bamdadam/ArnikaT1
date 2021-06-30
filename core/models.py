from django.db import models


# Create your models here.
class Company(models.Model):
    CompanyName = models.CharField(max_length=30)


# simple Financial model based of Financial data highlighted from PBGC's financial statements
# for the periods ending September 30, 1992 through September 30, 2009.
# https://data.world/finance/pbgc-financial-summary-data
# at the moment we dont have any particular data dependency between tables
class FinancialSummary(models.Model):
    NetIncome = models.IntegerField()
    Year = models.PositiveIntegerField()
    Company = models.ForeignKey(Company, related_name='FinancialSummary', on_delete=models.CASCADE,)

    class Meta:
        unique_together = ['Company', 'Year']

    def __str__(self):
        return 'ok'

# class FinancialPosition(models.Model):
#     CashAndInvestments = models.IntegerField()
#     TotalAssets = models.IntegerField()
#     NetPosition = models.IntegerField()
#     FinancialSummary = models.OneToOneField(FinancialSummary, on_delete=models.CASCADE)
