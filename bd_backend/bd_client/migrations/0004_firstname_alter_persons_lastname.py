# Generated by Django 4.0 on 2021-12-26 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bd_client', '0003_persons_address_persons_email_persons_surname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Firstname',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='persons',
            name='lastname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bd_client.firstname'),
        ),
    ]
