# Generated by Django 4.0.4 on 2022-05-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_alter_images_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(choices=[('Nature', 'Nature'), ('Vehicles', 'Vehicles'), ('People', 'People'), ('Travel', 'Travel'), ('Food', 'Food'), ('People', 'People'), ('Sky', 'Sky'), ('Animals', 'Animals')], max_length=12),
        ),
    ]
