import RPi.GPIO as GPIO
import json
import time
from datetime import datetime
import sys


class SignalSender:
    def __init__(self, signal_file):
        self.signals = None
        self.durations = None
        self.signal_file = signal_file
        self.load_data_from_files()
    
    def load_data_from_files(self):
        with open(self.signal_file) as file:
            signal_properties = json.load(file)
        self.signals = signal_properties.get("signal")
        self.durations = signal_properties.get("duration")

    def run_transmitter(self, sender_pin, mode):
        GPIO.setmode(mode)
        GPIO.setup(sender_pin, GPIO.OUT)
        for index in range(len(self.signals)):
            GPIO.output(sender_pin, self.signals[index])
            time.sleep(self.durations[index])
        GPIO.cleanup()
