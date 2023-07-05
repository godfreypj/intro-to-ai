"""
Module: Timer
Description: Functionality so each agent can have their own timer
"""
import time


class Timer:
    "Sets up a timer, in seconds."

    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        "Start time"
        self.start_time = time.time()

    def stop(self):
        "End time"
        self.end_time = time.time()

    def get_elapsed_time(self):
        "Return time from when start is called"
        if self.start_time is not None:
            if self.end_time is not None:
                return self.end_time - self.start_time
            else:
                return time.time() - self.start_time
        else:
            return None
