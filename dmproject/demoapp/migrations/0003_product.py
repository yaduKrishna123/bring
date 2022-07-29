# Generated by Django 3.2.13 on 2022-07-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_rename_about_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('img', models.ImageField(upload_to='img2')),
                ('dec', models.TextField()),
                ('link', models.URLField()),
            ],
        ),
    ]
