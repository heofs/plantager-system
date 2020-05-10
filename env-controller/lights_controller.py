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
        self.plan = plan
        self.event_loop = asyncio.get_event_loop()

    def run(self):
        self.task = self.event_loop.create_task(self.run_plan())
        self.event_loop.run_forever()

    def start_cycle(self):
        self.task = self.event_loop.create_task(self.run_plan())

    def set_plan(self, plan):
        print("setting plan to: ", plan)
        self.task.cancel()
        self.plan = plan
        self.task = self.event_loop.create_task(self.run_plan())
        asyncio.ensure_future(self.task, loop=self.event_loop)
        print("Finished set plan")

    def set_lights(self, state):
        logging.info(f'Turning lights {state}')

    async def run_plan(self):
        '''
        Takes in a light cycle plan in the form of a JSON object, and decide which cycle to run.
        '''
        print("Running plan")
        base_cycle = self.plan[0]
        while True:
            if (len(self.plan) == 1):
                await self.run_cycle(base_cycle)
            else:
                # Check other plans
                date_plans = self.plan[1:]
                for cycle in date_plans:
                    curr_date = datetime.now().date()

                    # Create DT object of current cycle date
                    cycle_dates = [
                        int(string) for string in cycle["date"].split('-')
                    ]
                    cycle_date = date(*cycle_dates)

                    # Check if next cycle date is active
                    if (self.plan.index(cycle) < len(date_plans)):
                        next_cycle = date_plans[self.plan.index(cycle)]
                        next_cycle_dates = [
                            int(string)
                            for string in next_cycle['date'].split('-')
                        ]
                        next_cycle_date = date(*next_cycle_dates)

                        # Continue to next cycle if it is within range
                        if (curr_date >= next_cycle_date):
                            continue

                    if (curr_date >= cycle_date):
                        await self.run_cycle(cycle)
                    else:
                        await self.run_cycle(base_cycle)
                    break

                # # Remove this break
                # break

    async def run_cycle(self, cycle):
        '''
        Runs the desired light cycle.
        '''
        print("Running cycle")
        logging.info(f'Activating cycle {str(cycle)}')

        curr_dt = datetime.now()
        today = (curr_dt.year, curr_dt.month, curr_dt.day)

        on_time = datetime(*today, cycle['on'][0], cycle['on'][1])

        on_diff = on_time - curr_dt
        secs_to_on = on_diff.total_seconds()

        # Handle turn on lights
        if (secs_to_on >= 0):
            self.set_lights("off")
            print("Turning lights on in: ", secs_to_on / 3600, ' hours')
            await asyncio.sleep(secs_to_on)
            self.set_lights("on")

        # Prevents turnoff lights till midnight, and sleeps till next day.
        if (cycle['off'][0] == 24):
            await self.sleep_to_next_day()
            return

        # Handle when to turn of lights and how long.
        curr_dt = datetime.now()
        off_time = datetime(*today, cycle['off'][0], cycle['off'][1])
        off_diff = off_time - curr_dt
        secs_to_off = off_diff.total_seconds()
        print("secs to off", secs_to_off)
        if (secs_to_off >= 0):
            self.set_lights("on")
            print("Turning lights off in: ", secs_to_off / 3600, ' hours')
            await asyncio.sleep(secs_to_off)
            self.set_lights("off")

        await self.sleep_to_next_day()

    async def sleep_to_next_day(self):
        curr_dt = datetime.now()

        today = (curr_dt.year, curr_dt.month, curr_dt.day)
        next_day = datetime(*today, hour=0, minute=0) + timedelta(days=1)

        day_diff = next_day - curr_dt
        secs_to_next_day = day_diff.total_seconds()
        print("secs to next day: ", secs_to_next_day)
        await asyncio.sleep(secs_to_next_day)


if __name__ == "__main__":
    import time
    lights_plan = [{
        "date": "start",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-10",
        "on": [16, 39],
        "off": [16, 40]
    }, {
        "date": "2020-05-15",
        "on": [6, 0],
        "off": [22, 0]
    }]

    light_controller = LightsController(lights_plan)
    light_controller.start()
    time.sleep(1)
    light_controller.set_plan([{
        "date": "start",
        "on": [16, 33],
        "off": [22, 1]
    }])
