# Generated by Django 4.2.5 on 2023-09-26 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeadsTails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rest_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('res', models.CharField(default=True, max_length=50)),
            ],
        ),
    ]
