# Generated by Django 3.1.7 on 2021-03-05 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коммент'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Пост'},
        ),
        migrations.AddField(
            model_name='comment',
            name='child',
            field=models.BooleanField(default=False),
        ),
    ]
