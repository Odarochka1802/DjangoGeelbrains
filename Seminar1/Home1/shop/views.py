import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)


def index(request):
    logger.info("OK")
    info = """
    <!DOCTYPE html>
<html>
<head>
    <title>Название вашего интернет-магазина</title>
    <link rel="stylesheet" href="style.css"> <!-- Подключение внешнего CSS-файла для стилизации страницы -->
</head>
<body style="font-family: Arial, sans-serif;line-height: 1.5;background-color: #f5f5f5;  margin: 0;padding: 0;box-sizing: border-box">
    <header style="background-color: #333;padding: 20px;color: #fff;">
        <h1 style="margin-bottom: 10px;">Добро пожаловать в наш интернет-магазин!</h1>
        <nav>
            <ul style="list-style-type: none;">
                <li style="display: inline-block;margin-right: 15px;"><a style="text-decoration: none;color: #fff;" href="#">Главная</a></li>
                <li style="display: inline-block;margin-right: 15px;><a  style="text-decoration: none;color: #fff;" href="#">Каталог</a></li>
                <li style="display: inline-block;margin-right: 15px;><a  style="text-decoration: none;color: #fff;" href="#">О нас</a></li>
                <li style="display: inline-block;margin-right: 15px;><a  style="text-decoration: none;color: #fff;" href="#">Контакты</a></li>
            </ul>
        </nav>
    </header>
    <main style="padding: 20px;">
        <section class="banner" style="margin-bottom: 30px; background-color: #f9f9f9;padding: 30px;text-align: center;">
            <h2 style="margin-bottom: 10px;">Акционные предложения!</h2>
            <p style="margin-bottom: 20px;">У нас есть лучшие товары по низким ценам. Поторопитесь сделать заказ!</p>
            <a href="#" class="btn" style="display: inline-block;padding: 10px 20px;background-color: #333;color: #fff;text-decoration: none;border-radius: 5px;">Купить сейчас</a>
        </section>
        <section class="featured-products" style="display: flex;flex-wrap: wrap;">
            <h2 style="margin-bottom: 10px;">Популярные товары</h2>
            <div class="product" style="width: 25%;padding: 10px;text-align: center;>
                <img src="product1.jpg" alt="Товар 1" style="width: 100%;max-height: 200px;object-fit: cover;margin-bottom: 10px;">
                <h3 style="margin-bottom: 5px;">Название товара</h3>
                <p style="margin-bottom: 20px;">Цена: $99.99</p>
                <a href="#" class="btn" style="display: inline-block;padding: 10px 20px;background-color: #333;color: #fff;text-decoration: none;border-radius: 5px;">Подробнее</a>
            </div>
            <!-- Добавьте другие товары -->
            
        </section>
    </main>
    <footer style=" background-color: #333;color: #fff;padding: 20px;text-align: center;">
        <p>&copy; 2023 Мой интернет-магазин. Все права принадлежат мне))).</p>
        </div>
    </footer>
</body>
</html>
    """
    return HttpResponse(info)


def about(request):
    logger.info("about")
    info = """<!DOCTYPE HTML>
<html>
 <head>
  <meta charset="utf-8">
  <title>Тег А, атрибут target</title>
 </head>
 <body>
 <div style="width: 90%; border: 1px solid #333; box-shadow: 8px 8px 5px #444; padding: 8px 12px; background-image: linear-gradient(180deg, #fff, #ddd 40%, #ccc)"> 
 <h1>Добро пожаловать в наш интернет-магазин!</h1>
</div>
 <div class="container">
  <p style="padding: 20px;">Здесь вы найдете широкий выбор качественных товаров по отличным ценам. <br>Наш интернет-магазин предлагает разнообразие 
  продуктов для всех возрастных категорий и интересов. У нас вы можете найти модную одежду, стильные аксессуары, косметику, 
  товары для дома, электронику и многое другое. Мы тщательно подбираем товары, чтобы обеспечить высокое качество и удовлетворить потребности наших клиентов.</p>
<p>Независимо от того, что вас интересует - модный стиль, функциональность или красота - наш интернет-магазин предлагает 
разнообразие опций для удовлетворения ваших потребностей. Мы постоянно обновляем наш ассортимент, чтобы предложить вам новые и новейшие товары.</p>
<p>Мы стремимся предоставить непревзойденный уровень обслуживания наших клиентов. Наша команда всегда готова помочь вам в 
выборе товара, ответить на ваши вопросы и обеспечить приятный опыт покупок в нашем магазине.</p>
<p>Оформление заказа у нас легкое и безопасное. Мы гарантируем безопасность ваших платежей и конфиденциальность вашей информации.</p>
<p>Мы ценим каждого клиента и стремимся к высокому уровню удовлетворенности. Ваше мнение очень важно для нас, поэтому мы 
всегда открыты к обратной связи, предложениям и комментариям.</p>
<p>Мы приглашаем вас ознакомиться с нашим ассортиментом и найти то, что идеально подойдет именно для вас. Благодарим вас за выбор нашего интернет-магазина и желаем вам приятных покупок!</p>
 </div>
 <footer style=" background-color: #333;color: #fff;padding: 20px;text-align: center;">
        <p>&copy; 2023 Мой интернет-магазин. Все права принадлежат мне))).</p>
        </div>
    </footer>
 </body>
</html>"""
    return HttpResponse(info)
