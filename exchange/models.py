import uuid

from django.db import models
from django.utils import timezone
from django.urls import reverse

class Product(models.Model):
    class Meta:
        permissions = (('can_edit_product', "create or update a product"),)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='images/', blank=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def was_created_recently(self):
        now = timezone.now()
        return now >= self.created_at >= now - datetime.timedelta(days=7)
    def get_absolute_url(self):
        return reverse('exchange:product-detail', args=[str(self.id)])

#    def get_absolute_url(self):
#        return reverse('product-detail', )
