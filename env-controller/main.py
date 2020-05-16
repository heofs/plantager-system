#! /usr/bin/env python3
# countasync.py

import time
import json
from database import UserDB
from lights_controller import LightsController
from subscriber import Subscriber

exchange_name = 'lights-cycle'

db = UserDB()


def get_plan():
    plan = db.get_setting('light_cycle')
    return json.loads(plan["setting"])


lights_plan = get_plan()
print("got plan")
lights_controller = LightsController(lights_plan)
lights_controller.start()

# def callback(plan):
#     print("retrieved plan -> %r" % plan)
#     lights_controller.set_plan(plan)

# try:
#     sub = Subscriber(callback, exchange_name=exchange_name)
#     sub.start_consuming()

# except (KeyboardInterrupt):
#     sub.close_connection()
#     print("\nClosed connection.")
