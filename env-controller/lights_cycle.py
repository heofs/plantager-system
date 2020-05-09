from datetime import datetime, timedelta, date


def set_lights(state):
    # print("Setting lights ", state)
    pass


def run_cycle(cycle):
    print("Activating cycle: ", cycle)
    curr_dt = datetime.now()
    today = (curr_dt.year, curr_dt.month, curr_dt.day)

    on_time = datetime(*today, cycle['on'][0], cycle['on'][1])

    on_diff = on_time - curr_dt
    secs_to_on = on_diff.total_seconds()

    #
    if (secs_to_on >= 0):
        print("Lights off")
        set_lights("off")
        print("Turning lights on in: ", secs_to_on / 3600, ' hours')
        # time.sleep(secs_to_on)
        set_lights("on")

    # Prevents turnoff lights till midnight, and sleeps till next day.
    if (cycle['off'][0] == 24):
        curr_dt = datetime(*today, hour=0, minute=0)
        next_day = curr_dt + timedelta(days=1)
        curr_dt = datetime.now()
        day_diff = next_day - curr_dt
        secs_to_next_day = day_diff.total_seconds()

        print("secs to next day: ", secs_to_next_day)
        # time.sleep(secs_to_next_day)

        return

    # Handle when to turn of lights and how long.
    off_time = datetime(*today, cycle['off'][0], cycle['off'][1])
    off_diff = off_time - curr_dt
    secs_to_off = off_diff.total_seconds()
    if (secs_to_on <= 0 and secs_to_off >= 0):
        print("Lights on")
        set_lights("on")
        print("Turning lights off in: ", secs_to_off / 3600, ' hours')
        # time.sleep(secs_to_off)
        set_lights("off")


def check_plan(plan):
    '''
    Takes in a light cycle plan in the form of a JSON object, and decide which cycle to activate.
    '''
    base_cycle = plan[0]
    while True:
        if (len(plan) == 1):
            print("Activating base cycle FIRST")
            run_cycle(base_cycle)
        else:
            # Check other plans
            date_plans = plan[1:]
            for cycle in date_plans:
                curr_date = datetime.now().date()

                # Create DT object of current cycle date
                cycle_dates = [
                    int(string) for string in cycle["date"].split('-')
                ]
                cycle_date = date(*cycle_dates)

                # Check if next cycle date is active
                if (plan.index(cycle) < len(date_plans)):
                    next_cycle = date_plans[plan.index(cycle)]
                    next_cycle_dates = [
                        int(string) for string in next_cycle['date'].split('-')
                    ]
                    next_cycle_date = date(*next_cycle_dates)

                    # Continue to next cycle if it is within range
                    if (curr_date >= next_cycle_date):
                        print("Skipping to next")
                        continue

                if (curr_date >= cycle_date):
                    print("Activating date cycle ONE")
                    run_cycle(cycle)
                else:
                    print("Activating base SECOND")
                    run_cycle(base_cycle)
                break

            break


if __name__ == "__main__":
    lights_plan = [{
        "date": "start",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-09",
        "on": [6, 0],
        "off": [22, 0]
    }, {
        "date": "2020-05-15",
        "on": [6, 0],
        "off": [22, 0]
    }]

    check_plan(lights_plan)