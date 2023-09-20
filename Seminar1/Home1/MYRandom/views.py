from random import random, choice, randint
import logging

logger = logging.getLogger(__name__)

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def one(request):
    logger.info("One page started")
    answer = ["Орёл", "Решка"]
    i = choice(answer)
    return HttpResponse(i)


def two(request):
    logger.info("Two page started")
    answer = randint(1, 6)
    return HttpResponse(answer)


def three(request):
    logger.info("Tree page started")
    return HttpResponse(randint(0, 100))
