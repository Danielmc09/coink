# Generated by Django 3.2 on 2022-09-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'register_user',
            },
        ),
    ]
