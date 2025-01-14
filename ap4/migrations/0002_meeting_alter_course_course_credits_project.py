# Generated by Django 5.0.6 on 2024-07-10 03:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap4', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_code', models.CharField(max_length=100)),
                ('meeting_dt', models.DateField(auto_now_add=True)),
                ('meeting_subject', models.CharField(max_length=100)),
                ('meeting_np', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='course_credits',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptopic', models.CharField(max_length=100)),
                ('planguages', models.CharField(max_length=100)),
                ('pduration', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ap4.student')),
            ],
        ),
    ]
