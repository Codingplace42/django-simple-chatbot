# Generated by Django 3.2 on 2021-05-01 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='method',
            field=models.CharField(blank=True, choices=[('Recomendation', 'simple_chatbot.responses.RecomendationResponse'), ('Greeting', 'simple_chatbot.responses.GreetingResponse')], max_length=120, verbose_name='Method'),
        ),
        migrations.AlterField(
            model_name='token',
            name='patterns',
            field=models.ManyToManyField(blank=True, editable=False, null=True, related_name='tokens', to='simple_chatbot.Pattern'),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(db_index=True, editable=False, max_length=40, unique=True, verbose_name='token'),
        ),
    ]