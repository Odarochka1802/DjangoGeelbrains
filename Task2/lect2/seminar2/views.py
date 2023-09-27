import random

from django.http import HttpResponse
from django.shortcuts import render
from random import random, choice, randint
import logging

from django.utils import timezone

from seminar2.models import HeadsTails



from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def heads(request):
        n = request.GET.get('n', '5')
        answer = ["Орёл", "Решка"]
        res = choice(answer)
        res_w = HeadsTails(res=res)
        res_w.save()
        data = HeadsTails.statistics(n)
        return HttpResponse(data.items())

