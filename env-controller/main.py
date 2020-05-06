#! /usr/bin/env python3
# countasync.py

import asyncio
import time
import threading

from subscriber import Subscriber

exchange_name = 'lights-cycle'

lights_plan = [{
    "date": "base",
    "start": "06:00",
    "stop": "21:00"
}, {
    "date": "04.05.2020",
    "start": "06:00",
    "stop": "21:00"
}]

import threading
import time
import asyncio


class Controller(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self._has_update = False
        self.cycle = 10

    def run(self):
        while not self._has_update:
            print("Running cycle")
            time.sleep(self.cycle)
        self.update()

    def update(self):
        print("detected update")
        self.cycle = 0.1
        self._has_update = False
        self.run()

    def set_cycle(self, new_cycle):
        self.cycle = new_cycle
        self._has_update = True


thread1 = Controller()

thread1.start()
time.sleep(5)
thread1.set_cycle(0.1)
