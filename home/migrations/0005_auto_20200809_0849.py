# Generated by Django 3.0.7 on 2020-08-09 05:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200809_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='firm',
            new_name='firms',
        ),
    ]
