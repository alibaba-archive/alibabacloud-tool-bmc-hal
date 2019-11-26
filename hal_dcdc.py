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
