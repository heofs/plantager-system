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
    def __init__(self):
        super(Controller, self).__init__()
        self._has_update = False
        self.cycle = 1
        self.event_loop = asyncio.get_event_loop()

    def run(self):
        try:
            self.task = self.event_loop.create_task(self.task_func())
            self.event_loop.run_forever()

        finally:
            self.event_loop.close()

    def start_cycle(self):
        self.task = self.event_loop.create_task(self.task_func())

    async def task_func(self):
        while True:
            print('Working... ')
            await asyncio.sleep(self.cycle)

    def set_cycle(self, new_cycle):
        print("setting cycle to", new_cycle)
        self.task.cancel()
        self.cycle = new_cycle
        self.task = self.event_loop.create_task(self.task_func())
        asyncio.ensure_future(self.task, loop=self.event_loop)


thread = Controller()
thread.start()
time.sleep(2)
thread.set_cycle(2)
time.sleep(1)
thread.set_cycle(1)
