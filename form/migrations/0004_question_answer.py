# Generated by Django 4.2.1 on 2023-06-04 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_question_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='Answer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Question_Answer', to='form.answer'),
            preserve_default=False,
        ),
    ]
