# Generated by Django 3.1.7 on 2021-04-08 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210408_1151'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='user',
        #     name='id',
        #     field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='user',
            name='compte',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.compte'),
        ),
    ]
