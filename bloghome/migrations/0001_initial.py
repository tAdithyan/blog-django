# Generated by Django 5.0 on 2023-12-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('thmbnail', models.ImageField(upload_to='blogimages')),
                ('created_at', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]