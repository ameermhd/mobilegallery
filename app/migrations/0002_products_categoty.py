# Generated by Django 3.2.5 on 2021-08-01 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='categoty',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.categ'),
            preserve_default=False,
        ),
    ]
