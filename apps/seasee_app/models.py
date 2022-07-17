from datetime import datetime, date

from apps.seasee_app.db import db, ma
from flask_marshmallow import fields
import geocoder


class Beach(db.Model):
    # テーブル名を指定する
    __tablename__ = "Beaches"
    __table_args__ = {"extend_existing": True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    prefecture = db.Column(db.String)
    address = db.Column(db.String)
    start_date = db.Column(db.Date, nullable=True)
    end_date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


class BeachSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Beach

    latlng = fields.fields.Method("address_to_latlng")
    is_open = fields.fields.Method("judge_open")

    def address_to_latlng(self, obj):
        address = obj.address
        ret = geocoder.osm(address, timeout=3.0)
        if ret.latlng:
            return ret.latlng
        else:
            return "Error"

    def judge_open(self, obj):
        flag = True if obj.start_date < date.today() < obj.end_date else False
        return flag
