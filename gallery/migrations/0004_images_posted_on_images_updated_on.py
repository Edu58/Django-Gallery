# Generated by Django 4.0.4 on 2022-05-28 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_alter_categories_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='images',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
