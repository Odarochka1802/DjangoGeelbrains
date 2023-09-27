import logging

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView

from shop.models import Client, Product, Order

# Create your views here.
logger = logging.getLogger(__name__)
menu = [
    {'title': "Главная", 'url_name': 'home'},
    {'title': "Каталог", 'url_name': 'catalog'},
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Контакты", 'url_name': 'contact'}
]


def index(request):
    logger.info("OK")

    return render(request, 'shop/index.html')


def catalog(request):
    logger.info("catalog")
    products = Product.objects.all()
    return render(request, 'shop/catalog.html',{'products':products})


def about(request):
    logger.info("about")
    return render(request, 'shop/about.html')


def contact(request):
    logger.info("contact")
    return render(request, 'shop/contact.html')


# Функция создания нового клиента
def create_client(name, email, phone, address):
    client = Client(name=name, email=email, phone=phone, address=address)
    client.save()


# Функция чтения информации о клиенте по его ID
def get_client(client_id):
    client = Client.objects.get(id=client_id)
    return client


# Функция обновления информации о клиенте
def update_client(client_id, new_name):
    client = Client.objects.get(id=client_id)
    client.name = new_name
    client.save()


# Функция удаления клиента
def delete_client(client_id):
    client = Client.objects.get(id=client_id)
    client.delete()


# Функция создания нового товара
def create_product(title, description, price, amount):
    product = Product(title=title, description=description, price=price, amount=amount)
    product.save()


# Функция чтения информации о товаре по его ID
def get_product(product_id):
    product = Product.objects.get(id=product_id)
    return product


# Функция обновления информации о товаре
def update_product(product_id, new_title):
    product = Product.objects.get(id=product_id)
    product.title = new_title
    product.save()


# Функция удаления товара
def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()


# Функция создания нового заказа
def create_order(client, products, total_amount):
    order = Order(client=client, total_amount=total_amount)
    order.save()
    order.products.set(products)


# Функция чтения информации о заказе по его ID
def get_order(order_id):
    order = Order.objects.get(id=order_id)
    return order


# Функция обновления информации о заказе
def update_order(order_id, new_total_amount):
    order = Order.objects.get(id=order_id)
    order.total_amount = new_total_amount
    order.save()


# Функция удаления заказа
def delete_order(order_id):
    order = Order.objects.get(id=order_id)
    order.delete()

class ShowProduct(DetailView):
    model = Product
    template_name = 'shop/product.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))

