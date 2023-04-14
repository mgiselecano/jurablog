# Generated by Django 4.2 on 2023-04-12 18:35

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0005_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Best_seller_author',
            fields=[
                ('author_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users_app.author')),
                ('best_seller_ranking', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('users_app.author',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]