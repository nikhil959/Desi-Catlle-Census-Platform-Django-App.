# Generated by Django 2.1 on 2018-10-30 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20181030_1059'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image2',
            new_name='Imageupload',
        ),
        migrations.RenameField(
            model_name='imageupload',
            old_name='img',
            new_name='img1',
        ),
        migrations.AlterModelTable(
            name='imageupload',
            table='image2',
        ),
    ]