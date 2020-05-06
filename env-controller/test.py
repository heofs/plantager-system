import threading
import time
import asyncio


class Controller(threading.Thread):
    def __init__(self, event_loop):
        super(Controller, self).__init__()
        self._has_update = False
        self.cycle = 1
        self.event_loop = event_loop

    def run(self):
        try:
            self.event_loop.run_until_complete(self.main())
        finally:
            self.event_loop.close()

    async def task_func(self):
        while True:
            print('Working...')
            await asyncio.sleep(1)

    async def main(self):
        print('creating task')
        self.task = self.event_loop.create_task(self.task_func())

        await asyncio.sleep(20)
        self.task_canceller()

    # async def change_cycle(self):
    #     self.task.cancel()
    #     print('canceled task')

    def task_canceller(self):
        self.task.cancel()
        print('canceled task')


event_loop = asyncio.get_event_loop()
# event_loop.stop()
thread = Controller(event_loop)
thread.start()
time.sleep(2)
thread.task_canceller()
print("Finished")
# thread.change_cycle()
# thread.set_cycle(0.1)
