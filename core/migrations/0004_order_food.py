# Generated by Django 4.1 on 2022-08-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='food',
            field=models.TextField(null=True),
        ),
    ]
