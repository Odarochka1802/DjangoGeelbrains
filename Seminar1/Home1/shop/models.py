from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images/", verbose_name="Изображение")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.PositiveIntegerField()
    time_create = models.DateField(auto_now_add=True)

    @property
    def photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    def __str__(self):
        return f'Title: {self.title}, description: {self.description}, price: {self.price}, amount: {self.amount}'


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_create = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Заказ от {self.client} на сумму {self.total_amount}"
