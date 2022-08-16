# Generated by Django 3.1 on 2022-08-16 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MTV', '0004_auto_20220812_1040'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mycar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MTV.car')),
            ],
        ),
    ]
