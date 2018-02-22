# Generated by Django 2.0.2 on 2018-02-22 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0004_vote_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='tokenset',
            options={'get_latest_by': 'created_at'},
        ),
        migrations.AlterUniqueTogether(
            name='option',
            unique_together={('vote', 'name')},
        ),
        migrations.AddField(
            model_name='tie',
            name='option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Meeting.Option'),
        ),
        migrations.AddField(
            model_name='tie',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Meeting.Vote'),
        ),
    ]
