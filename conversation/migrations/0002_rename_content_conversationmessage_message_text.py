# Generated by Django 5.0.6 on 2024-08-08 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='content',
            new_name='message_text',
        ),
    ]
