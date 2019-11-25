###############################################################################
#
# Hardware Abstraction Layer APIs -- BMC APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################

"""
class for HAL BMC APIs

"""


class HalBmc(object):
    def __init__(self):
        pass

    def get_info(self):
        """
        Get BMC info

        @return dict of BMC info or None for failure
                {
                    "Version": "1.1.1", # "N/A"
                    "Flash": "master",  # "N/A"
                    "Next": "master"    # "N/A"
                }
        """

    def get_version_all(self):
        """
        @return dict of BMCs
                {
                    "MasterVersion": "1.1.1",   # "N/A"
                    "SlaveVersion": "1.1.1"     # "N/A"
                }
        """
        pass

    def get_status(self):
        """
        Get BMC system status

        @return dict of system status or None for failure
                # "N/A" for invalid outpouts
                {
                    "CPU": {
                        "StateOutputs": "output of command 'top -bn 1'"
                        "Usage": "10.0"
                    },
                    "MEMORY": {
                        "StateOutputs": "output of command 'free -m'"
                        "Usage": "15.0"   # caculate: "free -t | grep \"buffers/cache\" | awk '{ printf \"mem usage  : %.1f%%\\n\",$3/($3+$4) * 100}'"
                    },
                    "DISK": {
                        "StateOutput": "output of command 'df -h'"
                        "Usage": "12.5"
                    }
                }
        """
        pass

    def get_next_boot(self):
        """
        Get next booting flash of BMC

        @return 'master'/'slave' on success, "N/A" for failure
        """
        pass

    def set_next_boot(self, flash):
        """
        Set flash from which next BMC boot

        @param flash Booting flash of BMC, "master" or "slave"

        @return 0 on success, -1 for failure
        """
        pass

    def reboot(self):
        """
        Reboot running BMC
        """
        pass
