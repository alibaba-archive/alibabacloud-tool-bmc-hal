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

    def set_system_led(self, color, blink=False):
        """
        Set system LED color, system LED indicates status of the whole system

        @param color The color of system fan LED, "green"/"yellow"/"off"
        @param blink True for blinking, False for steady

        @return 0 for success, -1 for failure
        """
        pass

    def system_power_led_available(self):
        """
        Get system power LED availability

        @return True if available, False otherwise.
        """
        pass

    def set_system_power_led(self, color, blink=False):
        """
        Set system power LED color, power LED indicates PSU, DC/DC status

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

    def get_cpld_user_reg(self):
        """
        Get user register value, 1 byte value

        @return unsigned value, 1 byte, None for failure
        """
        pass

    def set_cpld_user_reg(self, value):
        """
        Set user register value, 1 byte

        @return 0 for success, -1 for failure
        """
        pass

    def set_console_owner(self, owner):
        """
        Set console I/O owner

        @param owner I/O owner of the console, either "cpu" or "bmc"

        @return 0 for success, -1 for failure
        """
        pass

    def get_cpld_version(self):
        """
        Get version of CPLDs' that can be read from BMC

        @return dict of CPLDs' version or None for failure.
                example outputs:
                {
                    "BASE_CPLD": "0.1",     # or "N/A" for read failure
                    "FAN_CPLD": "0.2"
                }
        """
        pass

    def get_platform_name(self):
        """
        Get platform name

        @return platform name string, e.g. AS13-32H-F-$(VENDOR_NAME)
        """
        pass

    def get_sys_eeprom(self):
        """
        Get SYSEEPROM

        @return SYSEEPROM content dict or None for failure.
                example outputs:
                {
                    "Product Name": "AS23-128H",
                    "Product Manufacturer": "Manufacturer Name",
                    "Product Serial": "ABC0123456789",
                    "Product Part Number": "P10-F0001-01"

                    # Optional keys
                }
        @note value string should be "N/A" on read failure.
        """
        pass

    def execute_command(self, cmd_str):
        """
        Excute user specified command string.

        @param cmd_str command string from user

        @return (0, outputs) for success, (-1, outputs) for failure.
        """
        pass
