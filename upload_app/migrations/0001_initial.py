# Generated by Django 3.2.7 on 2023-05-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=11, verbose_name='文章名字')),
                ('data', models.FileField(upload_to='data')),
            ],
        ),
    ]
