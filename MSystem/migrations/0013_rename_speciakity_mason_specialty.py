# Generated by Django 5.1.4 on 2025-01-18 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MSystem', '0012_remove_customer_age_remove_customer_contact_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mason',
            old_name='speciakity',
            new_name='specialty',
        ),
    ]
