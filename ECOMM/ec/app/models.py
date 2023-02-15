from django.db import models
from django.contrib.auth.models import User
CATEGORY_CHOICES =(
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'Milkshake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
)

STATE_CHOICES = (
    ('HA TINH', 'HA TINH'),
    ('NGHE AN', 'NGHE AN'),
    ('NAM DIN', 'NAM DINH'),
    ('HAI PHONG', 'HA PHONG'),
    ('HCM', 'HCM'),
    ('DIEN BIEN', 'DIEN BIEN'),
    ('CAO BANG', 'CAO BANG'),
    ('LANG SON', 'LANG SON'),
    ('HA GIANG', 'HA GIANG'),
    ('THANH HOA', 'THANH HOA'),
    ('NINH BINH', 'NINH BINH'),
    ('QUANG NINH', 'QUANG NINH'),
    ('QUANG NAM', 'QUANG NAM'),
    ('HUE', 'HUE'),
    ('DA NANG', 'DA NANG'),
    ('THAI BINH', 'THAI BINH'),
    ('BAC NINH', 'BAC NINH'),
    ('NHA TRANG', 'NHA TRANG'),
    ('QUANG BINH', 'QUANG BINH'),
)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    
    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(default=0)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price
