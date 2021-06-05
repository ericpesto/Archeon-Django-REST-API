from django.db import models

# Create your models here

class StockActivity(models.Model):
    # activity_id = models.IntegerField(primary_key=True, blank=True)
    activity_id = models.AutoField(primary_key=True)
    # stock_code = models.CharField(blank=True, null=True, max_length=20)
    stock_code = models.ForeignKey(
        'stock.Stock',
        on_delete=models.CASCADE,
        related_name="stock_activities",
        blank=True, 
        null=True, 
        db_column='stock_code'
    )
    activity_date = models.DateTimeField(blank=True, null=True)
    # activity_type_id = models.IntegerField(blank=True, null=True)
    activity_type_id = models.ForeignKey(
        'activity_definitions.ActivityDefinition',
        on_delete=models.CASCADE,
        related_name="+",
        blank=True, 
        null=True, 
        db_column='activity_type_id'
    )
    client_name = models.TextField(blank=True, null=True)
    activity_amount_currency = models.TextField(blank=True, null=True)
    activity_amount = models.FloatField(blank=True, null=True)
    activity_comments = models.TextField(blank=True, null=True)
    expense_currency = models.TextField(blank=True, null=True)
    expense_pay_rate = models.FloatField(blank=True, null=True)
    und_expense_amount = models.FloatField(blank=True, null=True)
    acc_expense_amount = models.FloatField(blank=True, null=True)
    activity_update_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'stockactivities'

    def __str__(self):
        return f"{self.stock_code} ({self.activity_update_timestamp})"