# Generated by Django 3.0 on 2021-07-27 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210727_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Customer', verbose_name='Customer'),
        ),
    ]