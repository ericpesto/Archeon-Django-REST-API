from django.db import models

# Create your models here.
class ActivityDefinition(models.Model):
    activity_type_id = models.AutoField(primary_key=True)
    item_given_out = models.BooleanField(blank=True, null=True)
    includes_amount = models.BooleanField(blank=True, null=True)
    amount_name = models.TextField(blank=True, null=True)
    includes_expense = models.BooleanField(blank=True, null=True)
    # ! weirdddddd relationship with documentstatements, doc type to doc type
    # ? one-to-many? but why not lnked to primary key of document statements table
    document_type = models.TextField(blank=True, null=True)
    # document_type = models.ForeignKey(
    #     'document_statements.DocumentStatement', 
    #     on_delete=models.CASCADE,
    #     related_name='+', 
    #     blank=True, 
    #     null=True, 
    #     db_column='document_type'
    # )
    english = models.TextField(blank=True, null=True)
    dutch = models.TextField(blank=True, null=True)
    french = models.TextField(blank=True, null=True)
    german = models.TextField(blank=True, null=True)
    greek = models.TextField(blank=True, null=True)
    italian = models.TextField(blank=True, null=True)
    portuguese = models.TextField(blank=True, null=True)
    russian = models.TextField(blank=True, null=True)
    spanish = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'activitydefinitions'
    
    def __str__(self):
        return f"{self.english}"
