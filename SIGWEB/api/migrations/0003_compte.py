# Generated by Django 3.1.7 on 2021-04-07 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210405_2352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datecreation', models.DateTimeField(auto_now_add=True)),
                ('numerocompte', models.IntegerField()),
            ],
        ),
    ]