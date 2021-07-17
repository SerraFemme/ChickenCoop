import sched
import time
from datetime import datetime, timedelta
from threading import Timer


class DoorManager:
    def __init__(self):
        self.current_time = None
        self.system_power_status = True
        self.door_closed = True
        self.keep_door_closed = False
        self.scheduler = sched.scheduler(time.time, time.sleep)
        # self.morning_time = "06:00:00"
        # self.evening_time = "21:00:00"

        self.today = datetime.today()
        self.morning_time = self.today.replace(day=self.today.day, hour=6, minute=0, second=0, microsecond=0) + \
            timedelta(days=1)
        self.evening_time = self.today.replace(day=self.today.day, hour=21, minute=0, second=0, microsecond=0) + \
            timedelta(days=1)
        self.delta_morning = self.morning_time - self.today
        self.delta_evening = self.evening_time - self.today
        self.morning = self.delta_morning.total_seconds()
        self.evening = self.delta_evening.total_seconds()

    class DoorOpenDisabled(Exception):
        pass

    def is_system_on(self) -> bool:
        return self.system_power_status

    def turn_system_off(self):
        self.system_power_status = False

    def turn_system_on(self):
        self.system_power_status = True

    def is_door_closed(self):
        return self.door_closed

    def open_door(self):
        if self.keep_door_closed is True:
            raise self.DoorOpenDisabled
        self.door_closed = False

    def close_door(self):
        self.door_closed = True

    def disable_door_open(self):
        self.keep_door_closed = True

    def get_current_time(self):
        current_time = time.localtime()
        time_str = time.strftime("%H:%M:%S", current_time)
        return time_str

    def morning_operations(self):
        print("Rise and shine! Now git!")
        self.open_door()

    def evening_operations(self):
        print("Hit the sacks!")
        self.close_door()

    def start_schedule(self):
        morning_timer = Timer(self.morning, self.morning_operations)
        evening_timer = Timer(self.evening, self.evening_operations)

        morning_timer.start()
        evening_timer.start()
