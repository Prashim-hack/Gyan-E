# Generated by Django 3.2.10 on 2021-12-18 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_question_note_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/profiles/markdownx/'),
        ),
    ]