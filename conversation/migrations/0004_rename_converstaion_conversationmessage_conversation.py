# Generated by Django 5.0.6 on 2024-08-08 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0003_rename_message_text_conversationmessage_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversationmessage',
            old_name='converstaion',
            new_name='conversation',
        ),
    ]
