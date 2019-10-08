###############################################################################
#
# Hardware Abstraction Layer APIs -- CPU APIs.
#
# Copyright (C) Alibaba, INC.
#
###############################################################################


"""
class for HAL CPU APIs
"""
class HalCPU(object):
    def __init__(self):
        pass

    def get_state(self):
        """
        Get CPU current state.

        @return 'S0', ..., 'S5', or None for failure
        """
        pass

    def get_mca_error(self):
        """
        Get CPU MCA error count.

        @return List of MCERR and IERR counts, or None for failure
                Example:
                {
                    "MCErr": 0,
                    "IErr": 0
                }
        """
        pass

    def get_aer_error(self):
        """
        Get CPU AER error vector.

        @return List of AER error vector or None for failure
                Example:
                [ERR[0], ERR[1], ERR[2]]
        """
        pass

    def get_last_reset(self):
        """
        Get last CPU reset type, WARM/COLD.

        @return Last CPU reset type, "WARM"/"COLD", None for failure
        """
        pass
