# Generated by Django 3.0.8 on 2020-08-06 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0015_auto_20200806_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plateform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('console', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='game',
            name='trailer',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='plateform',
            field=models.ManyToManyField(to='game_api.Plateform'),
        ),
    ]
