# Generated by Django 3.0.8 on 2020-08-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0014_auto_20200806_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='test_img1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='test_img2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='test_img3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='test_img4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.RemoveField(
            model_name='game',
            name='test_img',
        ),
        migrations.AddField(
            model_name='game',
            name='test_img',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='TestImg',
        ),
    ]