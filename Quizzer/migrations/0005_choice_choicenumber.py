# Generated by Django 3.1.7 on 2021-05-25 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quizzer', '0004_auto_20210524_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='ChoiceNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
