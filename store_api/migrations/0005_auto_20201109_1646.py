# Generated by Django 3.1.3 on 2020-11-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0004_auto_20201109_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='date_added',
        ),
    ]