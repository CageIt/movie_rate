# Generated by Django 3.0.4 on 2020-04-13 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1)])),
                ('discuss', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('genre', models.CharField(blank=True, max_length=100, null=True)),
                ('producer', models.TextField(blank=True, null=True)),
                ('year', models.CharField(blank=True, max_length=4, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('feedback', models.ForeignKey(blank=True, default='NA', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='movie.Feedback')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movie.Movies'),
        ),
        migrations.AddField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
