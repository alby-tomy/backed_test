# Generated by Django 5.0.6 on 2024-06-21 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_alter_demomodel_gender_alter_demomodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demomodel',
            name='about_you',
            field=models.TextField(),
        ),
    ]
