# Generated by Django 4.2 on 2023-04-12 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_delete_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, default='Actualidad', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, default=None, max_length=200),
        ),
    ]
