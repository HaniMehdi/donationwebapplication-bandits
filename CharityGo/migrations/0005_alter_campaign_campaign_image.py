# Generated by Django 4.2 on 2023-05-24 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharityGo', '0004_alter_ngo_ngo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='campaign_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
