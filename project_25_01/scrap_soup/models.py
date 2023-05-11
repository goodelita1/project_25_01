from django.db import models
# Create your models here.

class AuthorName(models.Model):
    name = models.CharField(max_length = 1000)
    time = models.TimeField(null=True)
    
    def __str__(self):
        return self.name

class QuoteName(models.Model):
    name = models.CharField(max_length = 1000)
    quote_connect = models.ForeignKey('AuthorName', on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name