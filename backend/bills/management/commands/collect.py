import datetime
import json
import os

import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        bills = []
        count = 20
        results = True

        while results:
            resp = requests.get(f"https://api.propublica.org/congress/v1/117/both/bills/active.json?offset={count}",
                                headers={"X-API-Key": settings.PROPUBLICA_API})
            data = resp.json()

            for bill in data["results"][0]["bills"]:
                bills.append(bill)

            if data["results"][0]["num_results"] < 20:
                results = False
            else:
                count += 20

        json_string = json.dumps([bill for bill in bills], indent=2)

        dt = datetime.datetime.now()
        dt = dt.strftime("%Y-%d-%m")

        if not os.path.exists("data"):
            os.makedirs("data")

        with open(f"././data/{dt}.json", "w") as f:
            f.write(json_string)

        self.stdout.write(self.style.SUCCESS("Bill information has been extracted.\n"))
        self.stdout.write(self.style.SUCCESS(f"Total: {len(bills)}"))
