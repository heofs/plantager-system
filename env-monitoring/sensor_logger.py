from datetime import datetime, timedelta, date
import logging
import asyncio
import threading

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='sensor_monitoring.log',
                    level=logging.INFO)


class SensorMonitor(threading.Thread):
    def __init__(self):
        super(SensorMonitor, self).__init__()
        self._has_changed = False
        self.event_loop = asyncio.get_event_loop()
        self.interval = 30

    def run(self):
        self.task = self.event_loop.create_task(self.run_plan())
        self.event_loop.run_forever()

    async def sleeper(self, target_dt):
        while (datetime.now() < target_dt and not self._has_changed):
            print("Waiting....")
            await asyncio.sleep(1)

    async def run_plan(self):
        target_dt = datetime.now()
        print("RAN TARGET")
        while True:
            # get sensor value
            # post sensor value
            print("GETTING SENSOR VALUE")
            print("POSTING SENSOR VALUE")
            target_dt = target_dt + timedelta(seconds=self.interval)
            await self.sleeper(target_dt)

    def update_settings(self):
        self._has_changed = True


if __name__ == "__main__":
    import time

    sensor_monitor = SensorMonitor()
    sensor_monitor.start()
