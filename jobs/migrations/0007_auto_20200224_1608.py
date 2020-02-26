# Generated by Django 3.0.3 on 2020-02-24 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20200224_1605'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Job',
            new_name='JobPosting',
        ),
        migrations.AddField(
            model_name='applicant',
            name='job_posting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobs.JobPosting'),
        ),
        migrations.AlterModelTable(
            name='jobposting',
            table='job_postings',
        ),
    ]