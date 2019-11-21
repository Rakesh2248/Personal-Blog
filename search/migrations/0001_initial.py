# Generated by Django 2.2.5 on 2019-11-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=100)),
                ('search_count', models.PositiveIntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Search',
                'verbose_name_plural': 'searches',
            },
        ),
    ]
