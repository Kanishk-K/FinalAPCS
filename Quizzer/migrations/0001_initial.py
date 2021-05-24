# Generated by Django 3.1.7 on 2021-05-24 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QuestionNumber', models.IntegerField()),
                ('Prompt', models.CharField(max_length=200)),
                ('Explanation', models.TextField()),
                ('LinkedQuiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizzer.quiz')),
            ],
            options={
                'ordering': ['QuestionNumber'],
                'unique_together': {('LinkedQuiz', 'Prompt'), ('LinkedQuiz', 'QuestionNumber')},
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('LinkedQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quizzer.question')),
            ],
            options={
                'unique_together': {('LinkedQuestion', 'Text')},
            },
        ),
    ]