from django.db import models

# Create your models here.

class Name(models.Model):
    name_id = models.AutoField(primary_key=True)
    # name_id = models.IntegerField(primary_key=True, blank=True)
    name_type = models.CharField(max_length=50, blank=True, null=True, db_column='type')
    name = models.CharField(max_length=100,blank=True, null=True)
    linked_file = models.CharField(max_length=200,blank=True, null=True)

    class Meta:
        db_table = 'names'

    def __str__(self):
        return f"{self.name_id} - {self.name}"