#! /usr/bin/env python3
# countasync.py

import time
import json
import requests
from lights_controller import LightsController
from subscriber import Subscriber

exchange_name = 'light_plan'


def get_plan():
    res = requests.get("http://127.0.0.1:5000/settings",
                       data={'name': 'light_plan'})
    res = res.json()
    plan = res['value']
    return plan


lights_plan = get_plan()
lights_controller = LightsController(lights_plan)
lights_controller.start()


def callback(plan):
    print("retrieved plan -> %r" % plan)
    lights_controller.set_plan(plan)


try:
    sub = Subscriber(callback, exchange_name=exchange_name)
    sub.start_consuming()

except (KeyboardInterrupt):
    sub.close_connection()
    print("\nClosed connection.")
