# Generated by Django 2.2.6 on 2020-05-02 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='date1',
            field=models.DateField(null=True),
        ),
    ]
