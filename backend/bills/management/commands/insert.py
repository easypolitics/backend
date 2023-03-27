import datetime
import json

from django.conf import settings
from django.core.management.base import BaseCommand

from ...models import Bills

CONGRESS = settings.CONGRESS_VERSION
HOUSE = settings.HOUSE_BILLS
SENATE = settings.SENATE_BILLS


class Command(BaseCommand):
    def handle(self, *args, **options):
        dt = datetime.datetime.now()
        dt = dt.strftime("%Y-%m-%d")

        update_bills = []
        insert_bills = []

        with open(f"././data/{dt}.json", "r") as f:
            data = json.load(f)

            for bill in data:
                bill_id = Bills.objects.all().filter(bill_id=bill["bill_id"])

                obj = Bills(
                    bill_id=bill["bill_id"],
                    bill_slug=bill["bill_slug"],
                    bill_type=bill["bill_type"],
                    number=bill["number"],
                    bill_uri=bill["bill_uri"],
                    title=bill["title"],
                    short_title=bill["short_title"],
                    sponsor_title=bill["sponsor_title"],
                    sponsor_id=bill["sponsor_id"],
                    sponsor_name=bill["sponsor_name"],
                    sponsor_state=bill["sponsor_state"],
                    sponsor_party=bill["sponsor_party"],
                    sponsor_uri=bill["sponsor_uri"],
                    gpo_pdf_uri=bill["gpo_pdf_uri"],
                    congressdotgov_url=bill["congressdotgov_url"],
                    govtrack_url=bill["govtrack_url"],
                    introduced_date=bill["introduced_date"],
                    active=bill["active"],
                    last_vote=bill["last_vote"],
                    house_passage=bill["house_passage"],
                    senate_passage=bill["senate_passage"],
                    enacted=bill["enacted"],
                    vetoed=bill["vetoed"],
                    cosponsors=bill["cosponsors"],
                    cosponsors_by_party=bill["cosponsors_by_party"],
                    committees=bill["committees"],
                    committee_codes=bill["committee_codes"],
                    subcommittee_codes=bill["subcommittee_codes"],
                    primary_subject=bill["primary_subject"],
                    summary=bill["summary"],
                    summary_short=bill["summary_short"],
                    latest_major_action_date=bill["latest_major_action_date"],
                    latest_major_action=bill["latest_major_action"],
                    congress_version=CONGRESS
                )

                filtered_date, filtered_type = self.filtered_data(obj)
                obj.filtered_date, obj.filtered_type = filtered_date, filtered_type

                if bill_id:
                    update_bills.append(obj)
                else:
                    insert_bills.append(obj)

        update_bills = set(update_bills)
        insert_bills = set(insert_bills)

        Bills.objects.bulk_update(update_bills, [
            "bill_slug", "bill_type", "number", "bill_uri", "title", "short_title", "sponsor_title", "sponsor_id",
            "sponsor_name", "sponsor_state", "sponsor_party", "sponsor_uri", "gpo_pdf_uri", "congressdotgov_url",
            "govtrack_url", "introduced_date", "active", "last_vote", "house_passage", "senate_passage", "enacted",
            "vetoed", "cosponsors", "cosponsors_by_party", "committees", "committee_codes", "primary_subject",
            "summary", "summary_short", "latest_major_action_date", "latest_major_action", "filtered_date",
            "filtered_type", "congress_version"
        ], batch_size=500)

        Bills.objects.bulk_create(insert_bills, batch_size=500)

        self.stdout.write(self.style.SUCCESS("Bill information has been inserted into database.\n"))
        self.stdout.write(self.style.SUCCESS(f"Updated: {len(update_bills)}"))
        self.stdout.write(self.style.SUCCESS(f"Created: {len(insert_bills)}"))

    @staticmethod
    def filtered_data(obj):
        if obj.bill_type in SENATE:
            if obj.vetoed is not None:
                return obj.vetoed, "vetoed"
            elif obj.enacted is not None:
                return obj.enacted, "enacted"
            elif obj.house_passage is not None:
                return obj.house_passage, "house"
            elif obj.senate_passage is not None:
                return obj.senate_passage, "senate"
            else:
                return None, None
        elif obj.bill_type in HOUSE:
            if obj.vetoed is not None:
                return obj.vetoed, "vetoed"
            elif obj.enacted is not None:
                return obj.enacted, "enacted"
            elif obj.senate_passage is not None:
                return obj.senate_passage, "senate"
            elif obj.house_passage is not None:
                return obj.house_passage, "house"
            else:
                return None, None
        else:
            return None, None
