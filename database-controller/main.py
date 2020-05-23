from database import Database
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
db = Database()


@app.route('/sensors', methods=['GET', 'POST', 'DELETE'])
def sensors():
    # Add new sensor
    if request.method == 'POST':
        data = request.form
        db_res = db.add_sensor(data['sensor_id'], data['type'],
                               data['location'])
        if (db_res):
            return json.dumps({'success': True}), 200, {
                'ContentType': 'application/json'
            }
        return json.dumps({'success': False}), 400, {
            'ContentType': 'application/json'
        }

    # Delete sensor
    elif request.method == 'DELETE':
        data = request.form
        db_res = db.delete_sensor(data['sensor_id'])
        if (db_res):
            return json.dumps({'success': True}), 200, {
                'ContentType': 'application/json'
            }
        return json.dumps({'success': False}), 400, {
            'ContentType': 'application/json'
        }

    # Get sensor list
    else:
        sensor_list = db.get_sensor_list()
        return jsonify(sensor_list)


@app.route('/sensors/active', methods=['GET', 'POST', 'DELETE'])
def active_sensors():
    # Activate existing sensor
    if request.method == 'POST':
        data = request.form
        db_res = db.activate_sensor(data['sensor_id'])
        if (db_res):
            return json.dumps({'success': True}), 200, {
                'ContentType': 'application/json'
            }
        return json.dumps({'success': False}), 400, {
            'ContentType': 'application/json'
        }

    # Deactivate sensor
    elif request.method == 'DELETE':
        data = request.form
        db_res = db.deactivate_sensor(data['sensor_id'])
        if (db_res):
            return json.dumps({'success': True}), 200, {
                'ContentType': 'application/json'
            }
        return json.dumps({'success': False}), 400, {
            'ContentType': 'application/json'
        }

    # List active sensors
    else:
        sensor_list = db.get_active_sensors()
        return jsonify(sensor_list)


@app.route('/sensors/data', methods=['GET', 'POST'])
def sensor_data():
    # Insert sensor data
    if request.method == 'POST':
        data = request.form
        db_res = db.insert_data(data['sensor_id'], data['location'],
                                data['value'])
        if (db_res):
            return json.dumps({'success': True}), 200, {
                'ContentType': 'application/json'
            }
        return json.dumps({'success': False}), 400, {
            'ContentType': 'application/json'
        }

    # Get sensor data
    else:
        data = request.form
        sensor_data = db.get_data(data['sensor_id'])
        return jsonify(sensor_data)


@app.route('/settings', methods=['GET', 'PUT'])
def settings():
    if request.method == 'PUT':
        name = request.form['name']
        value = request.form['value']
        db_res = db.update_setting(name, value)
        return db_res
    else:
        name = request.form['name']
        db_res = db.get_setting(name)
        return db_res