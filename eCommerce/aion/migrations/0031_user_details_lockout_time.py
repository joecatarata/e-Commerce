# Generated by Django 2.0 on 2018-04-18 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aion', '0030_auto_20180418_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='lockout_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
