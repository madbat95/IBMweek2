# Generated by Django 3.2 on 2021-04-30 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='john', max_length=30)),
                ('last_name', models.CharField(default='doe', max_length=30)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]
