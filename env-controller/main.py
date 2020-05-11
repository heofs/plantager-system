#! /usr/bin/env python3
# countasync.py

import time

from lights_cycle import run_plan
from subscriber import Subscriber

exchange_name = 'lights-cycle'

import threading
import asyncio
import math


class Controller(threading.Thread):
    def __init__(self):
        super(Controller, self).__init__()
        self.cycle = 1
        self._has_changed = False
        self.event_loop = asyncio.get_event_loop()

    def run(self):
        self.task = self.event_loop.create_task(self.task_func())
        self.event_loop.run_forever()

    async def sleeper(self, delay):
        if (delay == 0 or delay < 0):
            return

        if (delay < 1):
            await asyncio.sleep(delay)
            return

        for _ in range(math.ceil(self.cycle)):
            await asyncio.sleep(1)
            if (self._has_changed):
                break

    async def task_func(self):
        while True:
            print('Working... ', self.cycle)

            await self.sleeper(self.cycle)
            if (self._has_changed):
                self._has_changed = False
                continue

    def set_cycle(self, new_cycle):
        print("setting cycle to", new_cycle)
        self.cycle = new_cycle
        self._has_changed = True


thread = Controller()
thread.start()
time.sleep(4)
thread.set_cycle(0.1)
time.sleep(1)
thread.set_cycle(2)

# time.sleep(1)
# thread.set_cycle(lights_plan)

# def callback(data):
#     # print("retrieved data -> %r" % data)
#     thread.set_cycle(lights_plan)

# try:
#     sub = Subscriber(callback, exchange_name=exchange_name)
#     sub.start_consuming()

# except (KeyboardInterrupt):
#     sub.close_connection()
#     print("\nClosed connection.")
