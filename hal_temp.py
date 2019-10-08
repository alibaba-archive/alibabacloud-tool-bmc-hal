###############################################################################
#
# Hardware Abstraction Layer APIs -- Temperature APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################


"""
class for HAL temperature APIs.

@param temp_dict: Dictionary of temperature, in Celcius degress and floating
                  point number.
                  Example:
                  {
                      "Value": 30.0,
                      "Min": -10.0,
                      "Max": 50.0
                  }
"""
class HalTemperature(object):
    def __init__(self):
        pass

    def get_cpu_temp(self):
        """
        Get CPU temperature.

        @return temp_dict for tempperature or None for failure
        """
        pass

    def get_inlet_temp(self):
        """
        Get Inlet temperature.

        @return temp_dict for tempperature or None for failure
        """
        pass

    def get_switch_temp(self):
        """
        Get Switch ASIC temperature.

        @return temp_dict for tempperature or None for failure
        """
        pass


