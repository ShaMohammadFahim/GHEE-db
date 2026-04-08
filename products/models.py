from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name

class Units(models.Model):
    type = models.CharField(max_length=100) 
    value = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.value} {self.type}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    size_value = models.CharField(max_length=50)
    unit = models.ForeignKey(Units, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.size_value} {self.unit.value}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')