# Generated by Django 3.0.5 on 2020-05-13 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20200513_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='notes',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
