# Generated by Django 3.2.10 on 2022-01-02 00:23

from django.db import migrations, models
import django_editorjs_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='note_editorjs',
            field=django_editorjs_fields.fields.EditorJsJSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='note_editorjs_text',
            field=django_editorjs_fields.fields.EditorJsTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]