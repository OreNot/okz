# Generated by Django 3.1 on 2020-08-14 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operatoranswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_title', models.CharField(max_length=255)),
                ('answer_description', models.TextField(null=True)),
                ('link1', models.CharField(max_length=555, null=True)),
                ('link2', models.CharField(max_length=555, null=True)),
                ('link3', models.CharField(max_length=555, null=True)),
                ('link4', models.CharField(max_length=555, null=True)),
                ('link5', models.CharField(max_length=555, null=True)),
                ('link6', models.CharField(max_length=555, null=True)),
                ('link7', models.CharField(max_length=555, null=True)),
                ('link8', models.CharField(max_length=555, null=True)),
                ('link9', models.CharField(max_length=555, null=True)),
                ('link10', models.CharField(max_length=555, null=True)),
            ],
        ),
    ]
