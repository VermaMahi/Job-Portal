# Generated by Django 5.0.4 on 2024-06-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_company_about_the_comapny'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='about_the_comapny',
        ),
        migrations.AddField(
            model_name='company',
            name='about_the_company',
            field=models.TextField(default='Default about text'),
        ),
    ]