# Generated by Django 3.2.19 on 2023-06-23 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_list', '0002_all_pro_list_pro_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_pro_list',
            name='pro_type',
            field=models.CharField(choices=[('gt', 'GENERAL')], default='gt', max_length=50, null=True),
        ),
    ]
