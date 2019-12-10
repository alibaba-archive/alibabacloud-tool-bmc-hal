###############################################################################
#
# Hardware Abstraction Layer APIs -- Temperature APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

import json
import os

HAL_SENSOR_DEFAULT_CONFIG_FILE = "/etc/sensors_config.json"

"""
class for HAL sensor APIs.

@param sensor_dict: Dict of sensor value
                    Example:
                    {
                        "Value": 30.0,      # -99999.0
                        "Min": -10.0,       # -99999.0
                        "Max": 50.0,        # -99999.0
                        "Unit": "C"         # "N/A"
                    }
@param name Name of a specific sensor
"""


class HalSensor(object):
    def __init__(self):
        self.config_file = HAL_SENSOR_DEFAULT_CONFIG_FILE
        if self.load_config() != 0:
            raise Exception("Load config file %s failed" % self.config_file)

    def load_config(self, config_file=None):
        """
        Load sensors configuration

        Configuration file is writen in JSON format. Mandatory keys:

        {
            "TEMPERATURE_SENSORS": {
                "Cpu": "sensor_name_for_cpu_temp",
                "Inlet": "sensor_name_for_inlet_temp",
                "Switch": "sensor_name_for_switch_temp"
            },
            "DCDC_SENSORS": {
                "DcdcInputVoltageName1": {
                    "Descr": "DCDC Input Voltage Name1 detailed description",
                    "Name": "sensor_name_for_dcdc_sensor_name1"
                },
                "DcdcInputCurrentName2": {
                    "Descr": "DCDC Input Current Name2 detailed description",
                    "Name": "sensor_name_for_dcdc_sensor_name2"
                },
                "DcdcOutputVoltageName3": {
                    "Descr": "DCDC Output Voltage Name3 detailed description",
                    "Name": "sensor_name_for_dcdc_sensor_name3"
                }
            }
        }

        @return 0 for success, -1 for failure
        """
        if config_file:
            self.config_file = config_file

        if not os.path.isfile(self.config_file):
            return -1

        with open(self.config_file) as fh:
            self.config = json.load(fh)

        return 0

    def get_sensor(self, name):
        """
        Get a specific sensor's info

        @return sensor_dict or None for failure
        """
        pass

    def get_sensor_info(self):
        """
        @return dict of sensors' information
                {
                    "SensorName1": {
                        "Value": 1.0,       # -99999.0
                        "Min": 0.0,         # -99999.0
                        "Max": 2.0,         # -99999.0
                        "Unit": "C"         # "N/A"
                    }
                }
        """
        pass
