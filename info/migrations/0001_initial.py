# Generated by Django 4.0.3 on 2022-06-17 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateField()),
                ('date_to', models.TimeField()),
                ('ad_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('ad_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='news_letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='news_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('des', models.TextField()),
                ('category', models.TextField()),
                ('youtube_link', models.URLField(max_length=300, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('email', models.EmailField(max_length=250)),
                ('mob_no', models.TextField(max_length=20)),
                ('comment', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.news_table')),
            ],
        ),
    ]
