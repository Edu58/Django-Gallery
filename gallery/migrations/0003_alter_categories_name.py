# Generated by Django 4.0.4 on 2022-05-28 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_categories_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(choices=[('Nature', 'Nature'), ('Vehicles', 'Vehicles'), ('People', 'People'), ('Sky', 'Sky'), ('Animals', 'Animals')], max_length=12),
        ),
    ]
