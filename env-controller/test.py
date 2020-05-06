import threading
import time
import asyncio


class Controller(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self._has_update = False
        self.cycle = 1

    def run(self):
        while not self._has_update:
            print("Running cycle")
            time.sleep(self.cycle)
        self.update_cycle()

    def update_cycle(self):
        print("detected update")
        self.cycle = 0.1
        self._has_update = False
        self.run()

    def set_cycle(self, new_cycle):
        self.cycle = new_cycle
        self._has_update = True


thread = Controller()

thread.start()
time.sleep(5)
thread.set_cycle(0.1)
