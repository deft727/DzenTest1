# Generated by Django 3.1.7 on 2021-03-05 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20210305_2237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date',
            new_name='timestamp',
        ),
    ]