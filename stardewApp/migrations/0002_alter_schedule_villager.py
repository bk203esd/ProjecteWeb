# Generated by Django 4.1.7 on 2023-03-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stardewApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='villager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villager', to='stardewApp.villager'),
        ),
    ]