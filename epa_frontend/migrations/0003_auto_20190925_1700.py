# Generated by Django 2.2.5 on 2019-09-25 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epa_frontend', '0002_merchants_merchant_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='merchants',
            old_name='admin_id',
            new_name='admin',
        ),
        migrations.RenameField(
            model_name='orderitems',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderitems',
            old_name='property_id',
            new_name='property',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='properties',
            old_name='merchant_id',
            new_name='merchant',
        ),
        migrations.RenameField(
            model_name='properties',
            old_name='property_type_id',
            new_name='property_type',
        ),
        migrations.RenameField(
            model_name='propertytype',
            old_name='merchant_id',
            new_name='merchant',
        ),
        migrations.AlterField(
            model_name='merchants',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]