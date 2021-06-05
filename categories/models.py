from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.TextField(blank=True, null=True)
    # category_id = models.IntegerField(primary_key=True, blank=True)
    category_id = models.AutoField(primary_key=True)
    # category_parent = models.IntegerField(blank=True, null=True)
    category_parent = models.ForeignKey(
        'categories.Category',
        on_delete=models.CASCADE,
        related_name="+", 
        blank=True, 
        null=True, 
        db_column='category_parent'
    )

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f"{self.category_id} - {self.category_name}"