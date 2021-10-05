# Generated by Django 3.2.7 on 2021-10-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=200)),
                ('year', models.IntegerField(blank=True, max_length=4)),
                ('price', models.FloatField(blank=True)),
                ('origin', models.CharField(max_length=200)),
                ('color', models.CharField(max_length=200)),
                ('horsepower', models.IntegerField(blank=True, max_length=4)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]