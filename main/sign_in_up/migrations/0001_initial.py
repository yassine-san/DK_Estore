# Generated by Django 3.2.19 on 2023-05-28 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email_id', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=550)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Customer login status',
                'verbose_name_plural': 'Customer login status',
            },
        ),
    ]
