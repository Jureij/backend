# Generated by Django 5.1.4 on 2024-12-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MSystem', '0008_alter_customer_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='mason',
            name='mobile_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
