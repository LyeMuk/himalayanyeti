# Generated by Django 4.1.4 on 2022-12-22 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_article_headerimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='label',
            name='parentcategory',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.categories'),
            preserve_default=False,
        ),
    ]
