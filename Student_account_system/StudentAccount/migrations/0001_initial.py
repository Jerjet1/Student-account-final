# Generated by Django 5.0.6 on 2024-05-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('birthday', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('contact_no', models.PositiveIntegerField()),
                ('year', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=25)),
            ],
        ),
    ]
