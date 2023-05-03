# Generated by Django 4.1.6 on 2023-02-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0003_rename_team_teams'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='teams',
        ),
    ]
