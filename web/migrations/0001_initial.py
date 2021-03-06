# Generated by Django 4.0.6 on 2022-07-15 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('original_url', models.CharField(max_length=1024)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('session', models.ForeignKey(db_column='session_key', on_delete=django.db.models.deletion.CASCADE, to='sessions.session')),
            ],
        ),
    ]
