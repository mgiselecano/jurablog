# Generated by Django 4.0.5 on 2023-04-13 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0007_author_pseudonym'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pseudonym',
            field=models.CharField(max_length=100),
        ),
    ]
