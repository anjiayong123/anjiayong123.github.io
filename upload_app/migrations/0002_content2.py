# Generated by Django 3.2.7 on 2023-07-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='data2')),
            ],
        ),
    ]
