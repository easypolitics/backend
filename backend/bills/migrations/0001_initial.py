# Generated by Django 4.1.3 on 2022-11-19 23:56

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('bill_id', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('bill_slug', models.CharField(max_length=255)),
                ('bill_type', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('bill_uri', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('short_title', models.TextField()),
                ('sponsor_title', models.CharField(max_length=255)),
                ('sponsor_id', models.CharField(max_length=255)),
                ('sponsor_name', models.CharField(max_length=255)),
                ('sponsor_state', models.CharField(max_length=255)),
                ('sponsor_party', models.CharField(max_length=255)),
                ('sponsor_uri', models.CharField(max_length=255, null=True)),
                ('gpo_pdf_uri', models.CharField(max_length=255, null=True)),
                ('congressdotgov_url', models.CharField(max_length=255, null=True)),
                ('govtrack_url', models.CharField(max_length=255, null=True)),
                ('introduced_date', models.CharField(max_length=255)),
                ('active', models.BooleanField()),
                ('last_vote', models.CharField(max_length=255, null=True)),
                ('house_passage', models.CharField(max_length=255, null=True)),
                ('senate_passage', models.CharField(max_length=255, null=True)),
                ('enacted', models.CharField(max_length=255, null=True)),
                ('vetoed', models.CharField(max_length=255, null=True)),
                ('filtered_date', models.CharField(max_length=255, null=True)),
                ('filtered_type', models.CharField(max_length=255, null=True)),
                ('cosponsors', models.CharField(max_length=255)),
                ('cosponsors_by_party', models.JSONField()),
                ('committees', models.CharField(max_length=255)),
                ('committee_codes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('subcommittee_codes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('primary_subject', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('summary_short', models.TextField()),
                ('latest_major_action_date', models.CharField(max_length=255)),
                ('latest_major_action', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'bill',
                'verbose_name_plural': 'bills',
                'db_table': 'bills',
            },
        ),
    ]
