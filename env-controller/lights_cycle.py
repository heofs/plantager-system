from datetime import datetime, timedelta


def set_lights(state):
    print("Setting lights ", state)


def check_timing(plan):
    while True:
        if (len(plan) == 1):
            cycle = plan[0]

            curr_dt = datetime.now()
            today = (curr_dt.year, curr_dt.month, curr_dt.day)

            on_time = datetime(*today, cycle['on'][0], cycle['on'][1])

            on_diff = on_time - curr_dt
            secs_to_on = on_diff.total_seconds()

            if (secs_to_on > 0):
                print("Lights off")
                set_lights("off")
                print("Turning lights on in: ", secs_to_on / 3600, ' hours')
                # time.sleep(secs_to_on)
                set_lights("on")

            if (cycle['off'][0] == 24):
                curr_dt = datetime(*today, hour=0, minute=0)
                next_day = curr_dt + timedelta(days=1)
                curr_dt = datetime.now()
                day_diff = next_day - curr_dt
                secs_to_next_day = day_diff.total_seconds()

                print("secs to next day: ", secs_to_next_day)
                continue

            off_time = datetime(*today, cycle['off'][0], cycle['off'][1])
            off_diff = off_time - curr_dt
            secs_to_off = off_diff.total_seconds()
            if (secs_to_on < 0 and secs_to_off > 0):
                print("Lights on")
                set_lights("on")
                print("Turning lights off in: ", secs_to_off / 3600, ' hours')
                # time.sleep(secs_to_off)
                set_lights("off")


if __name__ == "__main__":
    lights_plan = [
        {
            "date": "start",
            "on": [6, 0],
            "off": [24, 0]
        },
    ]
    # {
    #     "date": "2020.05.04",
    #     "start": "06:00",
    #     "stop": "21:00"
    # }
    # Loop through lights plan
    # Decide which plan is the active plan
    #

    check_timing(lights_plan)