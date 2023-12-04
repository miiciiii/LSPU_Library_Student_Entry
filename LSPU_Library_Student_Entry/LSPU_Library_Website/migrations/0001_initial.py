# Generated by Django 4.2.5 on 2023-11-29 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_full_name', models.CharField(max_length=100)),
                ('student_id', models.CharField(max_length=20, unique=True)),
                ('student_department', models.CharField(max_length=50)),
                ('student_course', models.CharField(max_length=50)),
                ('student_year', models.IntegerField()),
                ('student_qrcode_image', models.BinaryField(blank=True, null=True)),
            ],
        ),
    ]
