###############################################################################
#
# Hardware Abstraction Layer APIs -- Firmware APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

"""
class for HAL Firmware APIs.
"""


class HalFirmware(object):
    def __init__(self):
        pass

    def program_bios(self, flash, image):
        """
        Program BIOS flash with specific image

        @param flash 'master' or 'slave' BIOS flash
        @param image Absolute path of the BIOS image file

        @return 0 for success, -1 for failure
        """
        pass

    def get_bios_next_boot(self):
        """
        Get next booting flash of BIOS

        @return "master"/"slave" on success, "Failed" for failure
        """
        pass

    def set_bios_next_boot(self, flash):
        """
        Set flash from which next BIOS boot

        @param flash Booting flash of BIOS, "master" or "slave"

        @return 0 on success, -1 for failure
        """
        pass

    def program_bmc(self, flash, image):
        """
        Program BMC flash witch specific image

        @param flash 'master' or 'slave' BMC flash
        @param image Absolute path of BMC image file

        @return 0 for success, -1 for failure
        """
        pass

    def program_cpld(self, names, files):
        """
        Program CPLD

        @param names List of CPLD/FPGA names
        @param files List of refresh files for CPLD/FPGA

        @return 0 on success, -1 for failure
        """
        pass

    def refresh_firmware(self, names, files):
        """
        Refresh CPLD/FPGA/BIOS(reload ME) if applicable

        @param names List of CPLD/FPGA/BIOS names
        @param files List of refresh files for CPLD/FPGA

        @return 0 on success, -1 for failure
        """
        pass
