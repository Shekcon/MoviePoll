# Generated by Django 2.1.5 on 2019-01-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moviepoll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='moviepoll.Question'),
        ),
    ]
