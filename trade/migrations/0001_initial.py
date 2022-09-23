# Generated by Django 2.2 on 2021-06-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BacktestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('strategy', models.IntegerField()),
                ('parameter', models.TextField()),
                ('result', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('code', models.IntegerField()),
                ('amount', models.IntegerField(default=0)),
                ('buy_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SimAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('cash', models.FloatField(default=100000)),
            ],
        ),
        migrations.CreateModel(
            name='StockPool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('stock_list', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('code', models.TextField()),
                ('parameters', models.TextField()),
                ('is_public', models.BooleanField()),
            ],
        ),
    ]