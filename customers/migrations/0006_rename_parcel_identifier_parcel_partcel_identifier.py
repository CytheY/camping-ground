# Generated by Django 4.2.11 on 2024-04-17 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_parcel_remove_customer_place_id_delete_placeid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='parcel_identifier',
            new_name='partcel_identifier',
        ),
    ]
