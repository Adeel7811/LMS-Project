# Generated by Django 5.1.1 on 2024-09-11 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(choices=[('STUDENT', 'student'), ('TEACHER', 'teacher')], max_length=250)),
            ],
        ),
    ]
