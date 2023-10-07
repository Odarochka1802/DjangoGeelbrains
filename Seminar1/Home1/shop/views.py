import logging
from datetime import timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import DetailView

from shop.models import Client, Product, Order
from shop.forms import OrderForm, ProductForm

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
    products = Product.objects.all()

    return render(request, 'shop/index.html',{'products':products})


def catalog(request):
    logger.info("catalog")
    products = Product.objects.all()
    total = sum(products.amount for products in products)
    return render(request, 'shop/catalog.html',{'products':products,'total': total})


def about(request):
    logger.info("about")
    return render(request, 'shop/about.html')


def contact(request):
    logger.info("contact")
    return render(request, 'shop/contact.html')


def order_list(request, client_id):
    user_orders = Order.objects.filter(client_id=client_id)
    return render(request, 'shop/order_list.html', {'orders': user_orders})


# Функция создания нового клиента
def create_client(name, email, phone, address):
    client = Client(name=name, email=email, phone=phone, address=address)
    client.save()


# Функция чтения информации о клиенте по его ID
def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'shop/client_detail.html', {'client': client})


def client_list(request):
    clients = Client.objects.all()

    return render(request, 'shop/client_list.html', {'clients': clients})

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
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product_id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product_edit.html', {'form': form})


# Функция удаления товара
def delete_product(product_id):
    product = Product.objects.get(id=product_id)
    product.delete()


# Функция создания нового заказа
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            # Дополнительная обработка данных и создание заказа
            return redirect('order_success')
    else:
        form = OrderForm()

    return render(request, 'shop/order_form.html', {'form': form})

def order_success(request):
    return render(request, 'shop/order_success.html')


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

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})

