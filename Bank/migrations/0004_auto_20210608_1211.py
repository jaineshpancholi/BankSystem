# Generated by Django 3.1.4 on 2021-06-08 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_auto_20210608_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
