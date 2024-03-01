# Generated by Django 5.0.1 on 2024-01-22 07:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('category', models.ForeignKey(limit_choices_to={'name__in': ()}, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='app1.category')),
            ],
        ),
    ]