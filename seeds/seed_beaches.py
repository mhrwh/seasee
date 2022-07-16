from flask_seeder import Seeder, Faker, generator
from apps.seasee_app.app import Beach
from datetime import datetime, date
import random


class BeachSeeder(Seeder):

    # Refer: https://pypi.org/project/Flask-Seeder/
    # Lower priority will be run first.
    # All seeders with the same priority are then ordered by class name.
    # def __init__(self, db=None):
    #     super().__init__(db=db)
    #     self.priority = 1

    # run() will be called by Flask-Seeder
    def run(self):
        # Create a new Faker and tell it how to create User objects
        faker = Faker(
            cls=Beach,
            init={
                "id": generator.Sequence(),
                "name": generator.String("[a-z]\d{4}\c{3}"),
                "prefecture": "神奈川県",
                "address": "神奈川県茅ヶ崎市中海岸4丁目12986-5",
                "start_date": date(2021, random.randint(5, 8), random.randint(1, 30)),
                "end_date": date(2021, random.randint(5, 8), random.randint(1, 30)),
                "created_at": datetime.now(),
            },
        )

        # Create 3 beaches
        for beach in faker.create(3):
            print("Adding beach: %s" % beach)
            # Flask-Seeder will by default commit all changes to the database.
            self.db.session.add(beach)
