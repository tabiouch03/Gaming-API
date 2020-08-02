# Generated by Django 3.0.8 on 2020-08-02 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game_api', '0006_auto_20200801_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('resume', models.TextField()),
                ('image', models.CharField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
