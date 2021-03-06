# Generated by Django 2.0.4 on 2018-04-18 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20180415_2313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_total', models.FloatField()),
                ('order_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_waiting', to='orders.Customer')),
                ('order_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.Menu')),
            ],
        ),
    ]
