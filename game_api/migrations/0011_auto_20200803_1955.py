# Generated by Django 3.0.8 on 2020-08-03 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0010_auto_20200803_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='description3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_img',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_img1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_img2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_img3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='test_img4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
