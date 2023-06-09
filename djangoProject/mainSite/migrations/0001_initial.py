# Generated by Django 4.2 on 2023-04-30 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название альбома')),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('label', models.CharField(max_length=50, verbose_name='Лейбл')),
            ],
            options={
                'verbose_name': 'Альбом',
                'verbose_name_plural': 'Альбомы',
            },
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudonym', models.CharField(max_length=50, verbose_name='Псевдоним исполнителя')),
                ('genre', models.CharField(max_length=50, verbose_name='Жанр')),
                ('formed_in', models.DateField(verbose_name='Дата начала карьеры')),
                ('country', models.CharField(max_length=50, verbose_name='Страна')),
            ],
            options={
                'verbose_name': 'Исполнитель',
                'verbose_name_plural': 'Исполнители',
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название песни')),
                ('length', models.IntegerField(max_length=50, verbose_name='Продолжительность песни в секундах')),
                ('id_al', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainSite.albums')),
                ('id_ar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainSite.artists')),
            ],
            options={
                'verbose_name': 'Песня',
                'verbose_name_plural': 'Песни',
            },
        ),
        migrations.AddField(
            model_name='albums',
            name='id_ar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainSite.artists'),
        ),
    ]
