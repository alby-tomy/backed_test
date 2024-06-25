# Generated by Django 5.0.6 on 2024-06-21 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0003_alter_demomodel_about_you'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demomodel',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='demomodel',
            name='rating',
            field=models.CharField(choices=[('G', 'Good'), ('B', 'Bad')], default='G', max_length=1),
        ),
    ]
