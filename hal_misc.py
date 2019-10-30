###############################################################################
#
# Hardware Abstraction Layer APIs -- MISC APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

"""
class for HAL Misc APIs.
"""


class HalMisc(object):
    def __init__(self):
        pass

    def get_bios_boot_status(self):
        """
        Get lastest BIOS boot status, include boot_flash and result

        @return Dict of BIOS boot status or None for failure
                Example:
                {
                    "Flash": "master",      # "slave" or 'N/A'
                    "Result": "success"     # "failed" or 'N/A'
                }
        """
        pass

    def get_bmc_boot_status(self):
        """
        Get BMC latest boot status

        @return "master"/"slave" for boot successfully from master/slave flash
                "N/A" for read failed
        """
        pass

    def set_system_fan_led(self, color, blink=False):
        """
        Set system fan LED color

        @param color The color of system fan LED, "green"/"yellow"/"off"
        @param blink True for blinking, False for steady

        @return 0 for success, -1 for failure
        """
        pass

    def set_host_cpu_power(self, power_command):
        """
        Control host cpu power

        @param power_command Control command of host CPU's power,
                             should be "on"/"off"/"cycle"/"reset"

        @return 0 for success, -1 for failure
        """
        pass

    def get_host_cpu_power_status(self):
        """
        Get host cpu power status

        @return Power status of CPU(and affiliates), value should be
                "on"/"off", or "N/A" for failure
        """
        pass

    def set_location_led(self, cmd):
        """
        Set location LED admin status

        @param cmd Control command, "on"/"off"

        @return 0 for success, -1 for failure
        """
        pass

    def get_location_led(self):
        """
        Get location LED admin status

        @return status of location LED, "on"/"off" or "N/A" for failure
        """
        pass

    def get_system_airflow(self):
        """
        Get system air flow.

        @return "F2B"/"B2F" on success, "N/A" for failure
        """
        pass
