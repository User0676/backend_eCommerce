# Generated by Django 4.2.17 on 2024-12-11 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='order',
            index=models.Index(fields=['order_status'], name='orders_orde_order_s_33197f_idx'),
        ),
    ]
