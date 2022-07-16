from pathlib import Path

# Flaskクラスをimportする
from flask import Flask, render_template

from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()

# Flaskクラスをインスタンス化する
app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
    SQLALCHEMY_DATABASE_URI=(
        f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)


class Beach(db.Model):
    # ④テーブル名を指定する
    __tablename__ = "Beaches"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    prefecture = db.Column(db.String)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )


# SQLAlchemyとアプリを連携する
db.init_app(app)
# Migrateとアプリを連携する
Migrate(app, db)


# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return render_template("index.html")
