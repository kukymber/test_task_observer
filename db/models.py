from datetime import datetime

from db.engine import db


class CpuData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.now)
    cpu_utilization = db.Column(db.Float)
