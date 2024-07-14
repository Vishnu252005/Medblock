# Generated by Django 5.0.7 on 2024-07-13 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('allergies', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
    ]