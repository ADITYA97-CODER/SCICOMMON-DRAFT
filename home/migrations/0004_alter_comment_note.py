# Generated by Django 3.2.16 on 2023-04-01 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230401_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='note',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='home.note'),
        ),
    ]