# Generated by Django 3.2 on 2021-04-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customeruser_universitet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeruser',
            name='universitet',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]