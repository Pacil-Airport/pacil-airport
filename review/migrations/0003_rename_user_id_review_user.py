# Generated by Django 4.2.6 on 2023-10-27 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_remove_review_book_id_review_title_delete_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
