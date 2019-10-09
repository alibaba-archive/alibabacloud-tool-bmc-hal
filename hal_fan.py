###############################################################################
#
# Hardware Abstraction Layer APIs -- FAN APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################


"""
class for HAL Fan APIs

API parameters convention:

@param fan_name: Name of the specific fan, format: "FAN%d" % (fan_index),
                 where fan_index is integer starting from 1
@param rotor_index: Index of the specific  fan's rotor, integer starting from 1
"""


class HalFan(object):
    def __init__(self):
        pass

    def get_total_number(self):
        """
        Get total fan number count

        @return total number of fan in the system, -1 for failure
        """
        pass

    def get_rotor_number(self, fan_name):
        """
        Get fan's rotor count for specific fan_name

        @return total rotor count of specific fan, -1 for failure
        """
        pass

    def get_speed(self, fan_name, rotor_index):
        """
        Get current speed for specific fan and rotor

        @return speed of the specific fan and rotor, unit is RPM,
                -1 for failure
        """
        pass

    def set_speed(self, fan_name, rotor_index, speed):
        """
        Get current speed for specific fan and rotor

        @param speed of the specific fan and rotor, unit is RPM

        @return 0 for success, -1 for failure
        """
        pass

    def get_pwm(self, fan_name, rotor_index):
        """
        Get current PWM duty cycle for specific fan's specific rotor

        @return PWM duty cycle, unit is 1%, -1 for failure
        """
        pass

    def set_pwm(self, fan_name, rotor_index, pwm):
        """
        Set PWM for specific fan's specific rotor

        @param pwm duty cycle, unit is 1%, -1 for failure

        @return 0 for success, -1 for failure
        """
        pass

    def get_watchdog_status(self):
        """
        Get Fan watchdog status.

        @return 'Normal'/'Abnormal'/'Failed' for status good/bad/read-failed.
        """
        pass

    def set_led(self, fan_name, color, blink=False):
        """
        Set fan LED

        @param color The color of system fan LED, "green"/"yellow"/"off"
        @param blink True for blinking, False for steady

        @return 0 for success, -1 for failure
        """
        pass

    def get_info(self, fan_name):
        """
        Get specific fan's information

        @return dict for specific fan on success, None for failure
                Example return value(all keys are mandatory)
                {
                    # Properties
                    "Name": "FAN1",
                    "SN": "serial_number_example",
                    "PN": "part_number_exampple",
                    "Present": "yes"
                    "Rotors": 2,
                    "AirFlow": "F2B",
                    "SpeedMin": 2000,
                    "SpeedMax": 30000,

                    # Status, dynamic data
                    "Rotor1": {
                        "Running": "yes",
                        "HwAlarm": "no"
                        "Speed": 7000
                    },
                    "Rotor2": {
                        "Running": "yes",
                        "HwAlarm": "no"
                        "Speed": 8000
                    }
                }
        """
        pass

    def get_status(self, fan_name):
        """
        Get status of specific fan

        @return dict for specific fan for success, None for failure
                Example return value(all keys are mandatory)
                {
                    "Rotor1": {
                        "Running": "no",
                        "HwAlarm": "yes",
                        "speed": 0
                    },
                    "Rotor2": {
                        "Running": "yes",
                        "HwAlarm": "no",
                        "Speed": 6800
                    }
                }
        """
        pass

    def get_info_all(self):
        """
        Get all fans' info

        @return dict of all system fans' infor for success, None for failure
                Example return value(all keys are mandatory)
                {
                    "Number": 2,
                    "Watchdog": "NORMAL",
                    "FAN1": {
                        # Properties
                        "Name": FAN1,
                        "SN": "serial_number_example",
                        "PN": "part_number_exampple",
                        "Present": "yes"
                        "Rotors": 2,
                        "AirFlow": "F2B",
                        "SpeedMin": 2000,
                        "SpeedMax": 30000,

                        # Status, dynamic data
                        "Rotor1": {
                            "Running": "yes",
                            "HwAlarm": "no"
                            "Speed": 7000
                        },
                        "Rotor2": {
                            "Running": "yes",
                            "HwAlarm": "no"
                            "Speed": 8000
                        }
                    },
                    "FAN2": {
                        # Properties
                        "Name": FAN2,
                        "SN": "serial_number_example",
                        "PN": "part_number_exampple",
                        "Present": "yes"
                        "Rotors": 2,
                        "AirFlow": "F2B",
                        "SpeedMin": 2000,
                        "SpeedMax": 30000,

                        # Status, dynamic data
                        "Rotor1": {
                            "Running": "no",
                            "HwAlarm": "yes",
                            "Speed": 0
                        },
                        "Rotor2": {
                            "Running": "yes",
                            "HwAlarm": "no",
                            "Speed": 6800
                        }
                    }
                }
        """
        pass
