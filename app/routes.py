from flask import request, jsonify

from db.engine import app, db
from db.models import CpuData


@app.route('/cpu', methods=['POST'])
def receive_cpu_data():
    data = request.get_json()
    new_data = CpuData(cpu_utilization=data['cpu'])
    db.session.add(new_data)
    db.session.commit()
    return jsonify({"message": "Data received"}), 201


@app.route('/')
def index():
    pass
