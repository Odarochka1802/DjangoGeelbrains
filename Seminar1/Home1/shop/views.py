import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
logger = logging.getLogger(__name__)
def index(request):
    logger.info("OK")
    return HttpResponse("Hello World")
