# Generated by Django 5.1.7 on 2025-03-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jigyasa', '0002_remove_user_created_surveys_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='file_types',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='question',
            name='matrix_columns',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='question',
            name='matrix_rows',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('text', 'Text'), ('multiple_choice', 'Multiple Choice'), ('rating', 'Rating'), ('matrix', 'Matrix'), ('file_upload', 'File Upload')], max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='scale_labels',
            field=models.JSONField(blank=True, default=list),
        ),
    ]
