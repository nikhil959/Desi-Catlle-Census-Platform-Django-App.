# Generated by Django 2.1 on 2018-09-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_delete_newaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='newaccount2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('email', models.TextField()),
            ],
        ),
    ]