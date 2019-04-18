from django.db import models

# Create your models here.

class Bill_States(models.Model):
    """
    State of a bill:

    - Active: Bill is an active debt to be paid
    - Complete: Debt has been paid in full

    """
    name = models.CharField(max_length=10)


class Bills(models.Model):
    """
    Da Bills

    """
    name = models.CharField(max_length=25)
    start_amount = models.FloatField()
    zero_interest_date = models.DateField()
    biller_address = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    notes = models.CharField(max_length=255)
    web_link = models.CharField(max_length=255)
    # bill_state = models.ForeignKey(Bill_States, on_delete=models.PROTECT)


class Payments(models.Model):
    bill_id = models.ForeignKey(Bills, on_delete=models.PROTECT)
    payment_date = models.DateField()
    payment_amount = models.FloatField()


class IncomeSource(models.Model):
    source_name = models.CharField(max_length=20)


class Income(models.Model):
    source = models.ForeignKey(IncomeSource, on_delete=models.PROTECT)
    income_date = models.DateField()
    income_amount = models.FloatField()
