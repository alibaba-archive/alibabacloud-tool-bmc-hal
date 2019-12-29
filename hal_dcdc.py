###############################################################################
#
# Hardware Abstraction Layer APIs -- Temperature APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

HAL_DCDC_SENSOR = "DCDC_SENSORS"

"""
class for HAL DC/DC APIs.
"""


class HalDcdc(object):
    def __init__(self, sensor_obj):
        """
        @param sensor_obj Instance of HalSensor from hal_sensor module
        """
        self.sensors = sensor_obj

    def get_dcdc_sensors(self):
        sensor_dict = None
        dcdc_sensors = self.sensors.config[HAL_DCDC_SENSOR]
        if dcdc_sensors is not None:
            sensor_dict = {}
            for name in dcdc_sensors:
                sensor_dict[name] = dcdc_sensors[name]

        return sensor_dict

    def get_dcdc_sensor_value(self, name):
        """
        Get DCDC sonsor.

        @return voltage_dict for DCDC or None for failure
        """
        pass

    def get_dcdc_sensor_descr(self, name):
        """
        Get DCDC sensor's description.

        @return description string or None for failure
        """
        pass

    def get_dcdc_all_info(self):
        """
        Get all DCDC sensor info

        @return dict for all DCDC info or None for failure
        """
        pass
