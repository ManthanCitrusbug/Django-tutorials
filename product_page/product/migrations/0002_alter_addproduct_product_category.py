# Generated by Django 4.0.2 on 2022-03-16 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='product_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
    ]
