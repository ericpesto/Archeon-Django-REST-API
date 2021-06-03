from django.db import models

# Create your models here.
class StockLink(models.Model):
    link_id = models.AutoField(primary_key=True)
    # stock_code = models.CharField(blank=True, null=True, max_length=20)
    stock_code = models.ForeignKey(
        'stock.Stock',
        on_delete=models.CASCADE,
        related_name="stock_links",
        blank=True, 
        null=True,
        db_column='stock_code'
    )
    linked_file = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'stocklinks'

    def __str__(self):
        return f"{self.stock_code}"