from django.core.management import BaseCommand

from l2.models import User


class Command(BaseCommand):
    help = 'Create user'

    def handle(self, *args, **kwargs):
        user = User(name='John', email='egaw@ga.com', password='secret', age=25)
        user.save()
        self.stdout.write(f"{user}")

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'
