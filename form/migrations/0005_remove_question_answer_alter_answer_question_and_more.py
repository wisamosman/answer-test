# Generated by Django 4.2.1 on 2023-06-04 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='Answer',
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Question_Answer', to='form.question'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=300),
        ),
    ]
