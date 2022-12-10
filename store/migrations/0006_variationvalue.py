# Generated by Django 4.0.5 on 2022-12-01 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_productimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='VariationValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation', models.CharField(choices=[('size', 'size'), ('color', 'color')], max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('createdate', models.DateTimeField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]