import requests

# ADD NEW SENSOR
# payload = {'sensor_id': 's2', 'type': 'rh', 'location': 'floor'}
# r = requests.post("http://127.0.0.1:5000/sensors", data=payload)
# print(r.text)

# GET LIST OF EXISTING SENSORS
r = requests.get("http://127.0.0.1:5000/sensors")
print(r.text)

# GET LIST OF EXISTING SENSORS
# r = requests.delete("http://127.0.0.1:5000/sensors", data={'sensor_id': 's2'})
# print(r.text)

# LIST ACTIVE SENSORS
r = requests.get("http://127.0.0.1:5000/sensors/active")
print(r.text)

# ACTIVATE SENSOR
# r = requests.post("http://127.0.0.1:5000/sensors/active",
#                   data={'sensor_id': 's1'})
# print(r.text)

# DEACTIVATE SENSOR
# r = requests.delete("http://127.0.0.1:5000/sensors/active",
#                     data={'sensor_id': 's1'})
# print(r.text)

# INSERT SENSOR DATA
# r = requests.post("http://127.0.0.1:5000/sensors/data",
#                   data={
#                       'sensor_id': 's1',
#                       'location': 'canopy',
#                       'value': 22.2
#                   })
# print(r.text)

# GET SENSOR DATA
# r = requests.get("http://127.0.0.1:5000/sensors/data",
#                  data={'sensor_id': 's1'})
# print(r.text)

# GET SETTING
# r = requests.get("http://127.0.0.1:5000/settings", data={'name': 'light_plan'})
# print(r.text)

# UPDATE SETTING
import json
r = requests.put("http://127.0.0.1:5000/settings",
                 data={
                     'name':
                     'light_plan',
                     'value':
                     json.dumps([{
                         "date": "start",
                         "off": [21, 0],
                         "on": [9, 0]
                     }])
                 })
print(r.text)