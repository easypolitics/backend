from django.contrib.postgres.fields import ArrayField
from django.db import models


class Bills(models.Model):
    bill_id = models.CharField(primary_key=True, unique=True, max_length=255, blank=False, null=False)
    bill_slug = models.CharField(max_length=255, blank=True, null=True)
    bill_type = models.CharField(max_length=255, blank=True, null=True)
    number = models.CharField(max_length=255, blank=True, null=True)
    bill_uri = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    short_title = models.TextField(blank=True, null=True)
    sponsor_title = models.CharField(max_length=255, blank=True, null=True)
    sponsor_id = models.CharField(max_length=255, blank=True, null=True)
    sponsor_name = models.CharField(max_length=255, blank=True, null=True)
    sponsor_state = models.CharField(max_length=255, blank=True, null=True)
    sponsor_party = models.CharField(max_length=255, blank=True, null=True)
    sponsor_uri = models.CharField(max_length=255, blank=True, null=True)
    gpo_pdf_uri = models.CharField(max_length=255, blank=True, null=True)
    # noinspection SpellCheckingInspection
    congressdotgov_url = models.CharField(max_length=255, blank=True, null=True)
    govtrack_url = models.CharField(max_length=255, blank=True, null=True)
    introduced_date = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=False, null=False)
    last_vote = models.CharField(max_length=255, blank=True, null=True)
    house_passage = models.CharField(max_length=255, blank=True, null=True)
    senate_passage = models.CharField(max_length=255, blank=True, null=True)
    enacted = models.CharField(max_length=255, blank=True, null=True)
    vetoed = models.CharField(max_length=255, blank=True, null=True)
    cosponsors = models.CharField(max_length=255, blank=True, null=True)
    cosponsors_by_party = models.JSONField(blank=True, null=True)
    committees = models.CharField(max_length=255, blank=True, null=True)
    committee_codes = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    subcommittee_codes = ArrayField(models.CharField(max_length=255, blank=True, null=True), blank=True, null=True)
    primary_subject = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summary_short = models.TextField(blank=True, null=True)
    latest_major_action_date = models.CharField(max_length=255, blank=True, null=True)
    latest_major_action = models.TextField(blank=True, null=True)
    filtered_date = models.CharField(max_length=255, blank=True, null=True)
    filtered_type = models.CharField(max_length=255, blank=True, null=True)
    congress_version = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        db_table = "bills"
        verbose_name = "bill"
        verbose_name_plural = "bills"

    def __str__(self):
        return self.bill_id
