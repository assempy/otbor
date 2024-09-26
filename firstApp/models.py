from django.db import models
from django.utils import timezone

class Item(models.Model): 
    It_id = models.PositiveIntegerField() 
    It_name = models.CharField(max_length=50) 
    It_description = models.TextField(max_length=250) 
    It_price = models.CharField(max_length=50) 
    It_created_at = models.DateTimeField(auto_now=timezone.now) 
    def __str__(self): 
        return self.It_id
    def __str__(self) -> str: 
        return f'{self.It_created_at}'