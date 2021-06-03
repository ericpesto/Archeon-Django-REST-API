from django.db import models

# Create your models here.

class DocumentStatement(models.Model):
    statement_id = models.AutoField(primary_key=True)
    document_type = models.TextField(blank=True, null=True)
    statement_type = models.TextField(blank=True, null=True)
    includes_heading = models.BooleanField(blank=True, null=True)
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
        db_table = 'documentstatements'

    def __str__(self):
        return f"Document Type: {self.document_type} / Statement Type: {self.statement_type}"