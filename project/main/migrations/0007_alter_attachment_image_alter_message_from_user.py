# Generated by Django 4.0 on 2023-11-16 09:08

from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_timestamp_message_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=main.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages_from_me', to='main.conversation'),
        ),
    ]
