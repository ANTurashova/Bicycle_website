# Generated by Django 3.0.7 on 2020-08-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_product_tagline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.CharField(max_length=300, verbose_name='Описание'),
        ),
    ]
