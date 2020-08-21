# Generated by Django 3.1 on 2020-08-21 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BoardLI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='TITLE')),
                ('content', models.TextField(verbose_name='CONTENT')),
            ],
        ),
    ]
