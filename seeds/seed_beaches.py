from flask_seeder import Seeder, Faker, generator
from apps.seasee_app.app import Beach
from datetime import datetime, date
import random
from apps.seasee_app.prefectures import pre_list


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
                "prefecture": pre_list[random.randint(0, 46)],
                "address": "神奈川県茅ヶ崎市中海岸",
                "start_date": date(2021, random.randint(5, 7), random.randint(1, 30)),
                "end_date": date(2021, random.randint(8, 10), random.randint(1, 30)),
                "created_at": datetime.now(),
            },
        )

        # Create 3 beaches
        for i in range(10):
            for beach in faker.create():
                print("Adding beach: %s" % beach)
                # Flask-Seeder will by default commit all changes to the database.
                self.db.session.add(beach)
