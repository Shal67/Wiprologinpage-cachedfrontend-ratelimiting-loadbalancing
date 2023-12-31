# Generated by Django 4.2.4 on 2023-09-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KindleVersions',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('version', models.TextField(blank=True, null=True)),
                ('release_date', models.TextField(blank=True, null=True)),
                ('end_of_life_date', models.TextField(blank=True, null=True)),
                ('latest', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'kindle_versions',
                'managed': False,
            },
        ),
    ]
