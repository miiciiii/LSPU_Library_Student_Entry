# Generated by Django 4.2.5 on 2023-11-29 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LSPU_Library_Website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table_status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('occupied', 'Occupied'), ('vacant', 'Vacant')], max_length=10)),
            ],
        ),
    ]
