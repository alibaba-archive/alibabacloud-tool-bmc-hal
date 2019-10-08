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
                    "Flash": "master",
                    "Result": "sucess"
                }
        """
        pass

    def get_bmc_boot_status(self):
        """
        Get BMC last boot status

        @return "master"/"slave" for boot successfully from master/slave flash
        """
        pass

    def set_system_fan_led(self, color, blink):
        """
        Set system fan LED color

        @param color The color of system fan LED, "green"/"yellow"/"off"
        @param blink True for blinking, False for steady

        @return 0 for success, -1 for failure
        """
        pass


