from datetime import datetime, timedelta, date
import logging
import asyncio
import threading

logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='light_cycle.log',
                    level=logging.INFO)


class LightsController(threading.Thread):
    def __init__(self, plan):
        super(LightsController, self).__init__()
        self._has_changed = False
        self.plan = plan
        self.event_loop = asyncio.get_event_loop()
        self.set_lights("on")

    def run(self):
        self.task = self.event_loop.create_task(self.run_plan())
        self.event_loop.run_forever()

    def set_plan(self, plan):
        self.plan = plan
        self._has_changed = True

    def set_lights(self, state):
        if (self._has_changed):
            return
        logging.info(f'Turning lights {state}')

    async def sleeper(self, target_dt):
        while (datetime.now() < target_dt and not self._has_changed):
            print("Waiting....")
            await asyncio.sleep(1)

    async def run_plan(self):
        '''
        Takes in a light cycle plan in the form of a JSON object, and decide which cycle to run.
        '''
        while True:
            self._has_changed = False
            base_cycle = self.plan[0]
            if (len(self.plan) == 1):
                await self.run_cycle(base_cycle)
            else:
                # Check custom date plans
                date_plans = self.plan[1:]
                for cycle in date_plans:
                    curr_date = datetime.now().date()

                    # If next cycle date is active, skip current cycle
                    if (self.plan.index(cycle) < len(date_plans)):
                        next_cycle = date_plans[self.plan.index(cycle)]
                        next_cycle_dates = [
                            int(string)
                            for string in next_cycle['date'].split('-')
                        ]
                        next_cycle_date = date(*next_cycle_dates)

                        if (curr_date >= next_cycle_date):
                            continue

                    # Create DT object of current cycle date
                    cycle_dates = [
                        int(string) for string in cycle["date"].split('-')
                    ]
                    cycle_date = date(*cycle_dates)

                    if (curr_date >= cycle_date):
                        await self.run_cycle(cycle)
                    else:
                        await self.run_cycle(base_cycle)

                    break

    async def run_cycle(self, cycle):
        '''
        Runs the desired light cycle. One cycle is one day.
        '''
        if (self._has_changed):
            return
        print(f'Activating cycle {str(cycle)}')
        logging.info(f'Activating cycle {str(cycle)}')

        curr_dt = datetime.now()
        today = (curr_dt.year, curr_dt.month, curr_dt.day)

        on_dt = datetime(*today, cycle['on'][0], cycle['on'][1])

        # Handle turn on lights
        if (curr_dt < on_dt and not self._has_changed):
            self.set_lights("off")
            await self.sleeper(on_dt)
            self.set_lights("on")

        # Prevents turnoff lights till midnight, and sleeps till next day.
        if (cycle['off'][0] == 24 and not self._has_changed):
            await self.sleep_to_next_day()
            return

        # Handle when to turn off lights and how long.
        curr_dt = datetime.now()
        off_dt = datetime(*today, cycle['off'][0], cycle['off'][1])

        if (curr_dt < off_dt and not self._has_changed):
            self.set_lights("on")
            await self.sleeper(off_dt)
            self.set_lights("off")

        await self.sleep_to_next_day()

    async def sleep_to_next_day(self):
        curr_dt = datetime.now()
        today = (curr_dt.year, curr_dt.month, curr_dt.day)
        next_day = datetime(*today, hour=0, minute=0) + timedelta(days=1)
        await self.sleeper(next_day)


if __name__ == "__main__":
    import time
    lights_plan = [{
        "date": "start",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-09",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-11",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-13",
        "on": [6, 0],
        "off": [22, 0]
    }]

    light_controller = LightsController(lights_plan)
    light_controller.start()
    time.sleep(5)
    light_controller.set_plan([{
        "date": "start",
        "on": [14, 12],
        "off": [14, 14]
    }])
