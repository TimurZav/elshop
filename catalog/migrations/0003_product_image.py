# Generated by Django 4.0.1 on 2022-01-19 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=123, upload_to='upload/'),
            preserve_default=False,
        ),
    ]
