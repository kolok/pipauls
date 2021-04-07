from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField('creation date')
    def __str__(self):
        return self.name
    def was_created_recently(self):
        now = timezone.now()
        return now >= self.created_at >= now - datetime.timedelta(days=7)