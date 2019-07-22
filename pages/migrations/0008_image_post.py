# Generated by Django 2.1 on 2018-10-29 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_newaccount2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breedname', models.CharField(max_length=200)),
                ('counts', models.CharField(max_length=200)),
                ('ownername', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('aadharcard', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('animaltype', models.CharField(max_length=200)),
            ],
        ),
    ]