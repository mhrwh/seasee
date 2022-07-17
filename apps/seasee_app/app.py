from pathlib import Path

# Flaskクラスをimportする
from flask import Flask, render_template, jsonify

# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from flask_seeder import FlaskSeeder
from apps.seasee_app import db
from apps.seasee_app.models import Beach, BeachSchema
import json
from apps.seasee_app.prefectures import pre_list

# # SQLAlchemyをインスタンス化する
# db = SQLAlchemy()
# seeder = FlaskSeeder()

# Flaskクラスをインスタンス化する
app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
    SQLALCHEMY_DATABASE_URI=(
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_db(app)
db.init_ma(app)
db.init_seeder(app)

# # SQLAlchemyとアプリを連携する
# db.init_app(app)
# # Migrateとアプリを連携する
# Migrate(app, db)

# seeder.init_app(app, db)


def prefecture(i):
    beaches = Beach.query.filter_by(prefecture=pre_list[i]).all()
    beaches_schema = BeachSchema(many=True)
    ratio = 0
    count_open = 0
    for beach in beaches_schema.dump(beaches):
        if beach["is_open"]:
            count_open += 1
    count_all_beach = Beach.query.filter_by(prefecture=pre_list[i]).count()
    if count_all_beach:
        ratio = count_open / count_all_beach
    data = {
        "prefecture": pre_list[i],
        "prefecture_id": i + 1,
        "ratio": ratio,
        "beaches": beaches_schema.dump(beaches),
    }
    return data


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    prefectures = [prefecture(i) for i in range(47)]
    data = jsonify(
        {
            "status": "ok",
            "prefectures": prefectures,
        }
    )
    json_data = json.loads(data.data)
    return render_template("index.html", data=json_data)


if __name__ == "__main__":
    app.run(debug=True)
