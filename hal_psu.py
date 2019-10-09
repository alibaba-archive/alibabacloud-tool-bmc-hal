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

    def get_info(self, psu_name):
        """
        Get info of a specific PSU

        @return dict of the specific PSU's info, None for failure
                Example return value(all keys are mandatory)
                {
                    "Name": "PSU1",
                    "Present": "yes",
                    "SN": "serial_number_example",
                    "PN": "part_number_example",
                    "AirFlow": "B2F",

                    "InputType": "DC",
                    "InputStatus": True,
                    "OutputStatus": True
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
                    "Present": "yes",
                    "AirFlow": "F2B",
                    "InputType": "DC",
                    "InputStatus": True,
                    "OutputStatus": True
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
                        "Status": True,
                        "Type": "DC",
                        "Voltage": {
                            "Value": 220,
                            "LowAlarm": 200,
                            "HighAlarm": 240,
                            "Unit": "V"

                            # Optional
                            "LowWarning": 210,
                            "HighWarning": 230
                        },
                        "Current": {
                            "Value": 6.0,
                            "LowAlarm": 0.2,
                            "HighAlarm": 7.0,
                            "Unit": "A"

                            # Optional
                            "LowWarning": 0.3,
                            "HighWarning": 6.9
                        },
                        "Power": {
                            "Value": 1000,
                            "LowAlarm": 10,
                            "HighAlarm": 1400,
                            "Unit": "W"

                            # Optional
                            "LowWarning": 20,
                            "HighWarning": 1350
                        }
                    },
                    "Outputs": {
                        "Status": True,
                        "Voltage": {
                            "Value": 220,
                            "LowAlarm": 200,
                            "HighAlarm": 240,
                            "Unit": "V"

                            # Optional
                            "LowWarning": 210,
                            "HighWarning": 230
                        },
                        "Current": {
                            "Value": 6.0,
                            "LowAlarm": 0.2,
                            "HighAlarm": 7.0,
                            "Unit": "A"

                            # Optional
                            "LowWarning": 0.3,
                            "HighWarning": 6.9
                        },
                        "Power": {
                            "Value": 1000,
                            "LowAlarm": 10,
                            "HighAlarm": 1400,
                            "Unit": "W"

                            # Optional
                            "LowWarning": 20,
                            "HighWarning": 1350
                        }
                    }
                }
        """
        pass
