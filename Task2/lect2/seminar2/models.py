from django.db import models
from django.utils import timezone


class HeadsTails(models.Model):
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=50)

    @staticmethod
    def statistics(n):
        n = int(n)
        d = {"Орёл": 0, "Решка": 0}
        query = list(HeadsTails.objects.all())
        list_res = query[-n:]
        for item in list_res:
            if "Орёл" in str(item):
                d["Орёл"]+=1
            elif "Решка" in str(item):
                d['Решка']+=1
        return d

    def __str__(self):
        return f'time {self.rest_time} result {self.res}'
