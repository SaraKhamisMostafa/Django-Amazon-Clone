# Generated by Django 4.2.2 on 2023-07-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(verbose_name='rate'),
        ),
    ]
