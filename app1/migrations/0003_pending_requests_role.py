# Generated by Django 3.0.4 on 2020-03-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200310_1342'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_requests',
            name='role',
            field=models.CharField(default='Ta', max_length=50),
        ),
    ]