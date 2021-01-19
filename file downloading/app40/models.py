from django.db import models

class FileDetails(models.Model):
    fno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="my_document")