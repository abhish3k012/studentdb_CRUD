# Generated by Django 4.1.3 on 2022-12-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='s_marks',
            field=models.IntegerField(),
        ),
    ]