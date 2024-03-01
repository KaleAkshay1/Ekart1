# Generated by Django 5.0.1 on 2024-02-06 09:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_cart_price_alter_product_brand_alter_product_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(limit_choices_to={'name__in': ({'name': 'Allen Solly'}, {'name': 'Amazon Brand - INKAST'}, {'name': 'BRAND FLEX'}, {'name': 'Scott International'}, {'name': 'THE BLAZZE'}, {'name': 'U.S. POLO ASSN'})}, on_delete=django.db.models.deletion.CASCADE, to='app1.brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.ForeignKey(limit_choices_to={'name__in': ({'name': 'All'}, {'name': 'L'}, {'name': 'M'}, {'name': 'S'}, {'name': 'XL'}, {'name': 'XXL'})}, on_delete=django.db.models.deletion.CASCADE, to='app1.size'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(limit_choices_to={'name__in': ({'name': 'T-Shirts'}, {'name': 'Shirts'}, {'name': 'Sweaters'}, {'name': 'Hoodies'}, {'name': 'Sweatshirts'}, {'name': 'Tops'}, {'name': 'Tube Tops'}, {'name': 'Off-shoulder Tops'})}, on_delete=django.db.models.deletion.CASCADE, to='app1.subcategory'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='color',
            field=models.ForeignKey(limit_choices_to={'name__in': ({'name': 'Black'}, {'name': 'Blue'}, {'name': 'Brown'}, {'name': 'Gray'}, {'name': 'Green'}, {'name': 'Nevy Blue'}, {'name': 'Orange'}, {'name': 'Pink'}, {'name': 'Purple'}, {'name': 'Red'}, {'name': 'White'}, {'name': 'Yellow'})}, on_delete=django.db.models.deletion.CASCADE, to='app1.color'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(limit_choices_to={'name__in': ({'name': 'Bottom Wears'}, {'name': 'Top Wears'})}, on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='app1.category'),
        ),
    ]
