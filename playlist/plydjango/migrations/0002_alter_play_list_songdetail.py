# Generated by Django 4.0 on 2022-10-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plydjango', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play_list',
            name='songdetail',
            field=models.ManyToManyField(related_name='songlink', related_query_name='song', to='plydjango.song_detail'),
        ),
    ]
