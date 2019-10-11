###############################################################################
#
# Hardware Abstraction Layer APIs -- FAN APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

"""
class for HAL PSU APIs

API parameters convention:

@param psu_name Name of a PSU, format: "PSU%d" % psu_index, where psu_index is
                integer starting from 1
"""


class HalPsu(object):
    def __init__(self):
        pass

    def get_total_number(self):
        """
        Get system's total number of PSU

        @return Total number of PSU, -1 for failure
        """
        pass

    def get_presence(self, psu_name):
        """
        Get a specific PSU's presence status

        @return True if present, False for NOT present or failure
        """
        pass

    def get_fru_info(self, psu_name):
        """
        Get FRU info of a specific PSU

        @return dict of the specific PSU's info, None for failure
                Example return value(all keys are mandatory)
                {
                    "Name": "PSU1",
                    "SN": "serial_number_example",
                    "PN": "part_number_example",
                    "AirFlow": "B2F",
                }
        """
        pass

    def get_status(self, psu_name):
        """
        Get status of a specific PSU

        @return dict of the specific PSU's status, None for failure
                Example return value(all keys are mandatory)
                {
                    "Name": "PSU1",
                    "InputType": "DC",
                    "InputStatus": True,  # H/W status bit
                    "OutputStatus": True  # H/W status bit
                    "FanSpeed": {
                        "Value": 4000,
                        "Min": 2000,
                        "Max": 10000,
                    },
                    "Temperature": {
                        "Value": 40.0,
                        "Min": -30.0,
                        "Max": 50.0
                    }
                }
        """
        pass

    def get_power_status(self, psu_name):
        """
        Get power status of a specific PSU

        @return dict of the specific PSU's power status, None for failure
                Example return value
                {
                    "Name": "PSU1",
                    "Inputs": {
                        "Status": True, # H/W status bit
                        "Type": "DC",   # or "AC"
                        "Voltage": {
                            "Value": 220,
                            "LowAlarm": 200,
                            "HighAlarm": 240,
                            "Unit": "V"
                        },
                        "Current": {
                            "Value": 6.0,
                            "LowAlarm": 0.2,
                            "HighAlarm": 7.0,
                            "Unit": "A"
                        },
                        "Power": {
                            "Value": 1000,
                            "LowAlarm": -1,
                            "HighAlarm": 1400,
                            "Unit": "W"
                       }
                    },
                    "Outputs": {
                        "Status": True,
                        "Voltage": {
                            "Value": 220,
                            "LowAlarm": 200,
                            "HighAlarm": 240,
                            "Unit": "V"
                        },
                        "Current": {
                            "Value": 6.0,
                            "LowAlarm": 0.2,
                            "HighAlarm": 7.0,
                            "Unit": "A"
                        },
                        "Power": {
                            "Value": 1000,
                            "LowAlarm": -1,  # Don't care
                            "HighAlarm": 1400,
                            "Unit": "W"
                        }
                    }
                }
        """
        pass

    def set_fan_speed_pwm(self, psu_name, pwm):
        """
        Set a specific PSU's fan's speed

        @param pwm duty cycle, unit is 1%, -1 for failure

        @return 0 for success, -1 for failure
        """
        pass

    def get_info_all(self):
        """
        Get all system PSU's info

        @return dict of all PSUs or None for failure
                {
                    "Number": 2,
                    "PSU1": {
                        "SN": "serial_number_example",
                        "PN": "part_number_example",
                        "AirFlow": "F2B",

                        "FanSpeed": {
                            "Value": 4000,
                            "Min": 2000,
                            "Max": 30000
                        },
                        "Temperature": {
                            "Value": 35.0,
                            "Min": -20.0,
                            "Max": 45.0
                        },
                        "Inputs": {
                            "Status": True, # H/W status bit
                            "Type": "DC",   # or "AC"
                            "Voltage": {
                                "Value": 220,
                                "LowAlarm": 200,
                                "HighAlarm": 240,
                                "Unit": "V"
                            },
                            "Current": {
                                "Value": 6.0,
                                "LowAlarm": 0.2,
                                "HighAlarm": 7.0,
                                "Unit": "A"
                            },
                            "Power": {
                                "Value": 1000,
                                "LowAlarm": -1,
                                "HighAlarm": 1400,
                                "Unit": "W"
                           }
                        },
                        "Outputs": {
                            "Status": True,
                            "Voltage": {
                                "Value": 220,
                                "LowAlarm": 200,
                                "HighAlarm": 240,
                                "Unit": "V"
                            },
                            "Current": {
                                "Value": 6.0,
                                "LowAlarm": 0.2,
                                "HighAlarm": 7.0,
                                "Unit": "A"
                            },
                            "Power": {
                                "Value": 1000,
                                "LowAlarm": -1,  # Don't care
                                "HighAlarm": 1400,
                                "Unit": "W"
                            }
                        }
                    }
                }
        """
        pass
