# Generated by Django 3.0.2 on 2020-01-15 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200114_1531'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartline',
            old_name='cart_id',
            new_name='cart',
        ),
        migrations.RenameField(
            model_name='cartline',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='wishlistline',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='wishlistline',
            old_name='wishlist_id',
            new_name='wishlist',
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('OPEN', 'opens'), ('PAID', 'paid'), ('CANCEL', 'canceled')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='cart',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Cart'),
        ),
    ]
