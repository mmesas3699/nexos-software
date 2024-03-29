# Generated by Django 2.2.5 on 2019-11-19 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('value', models.PositiveIntegerField()),
                ('professor_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='professor', to='crud.Professor')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='crud.Student')),
            ],
        ),
    ]
