# Generated by Django 4.0 on 2022-10-14 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plydjango', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.AutoField(primary_key=True, serialize=False)),
                ('playlist_name', models.CharField(max_length=200, unique=True)),
                ('song', models.ManyToManyField(blank=True, related_name='play', to='plydjango.Song')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistSongMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_id', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plydjango.playlist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plydjango.song')),
            ],
            options={
                'ordering': ['map_id'],
            },
        ),
    ]