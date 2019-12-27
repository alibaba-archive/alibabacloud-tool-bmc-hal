#############################################
        BMC RESTful API definition
#############################################

1. BMC
   1.1 /api/bmc/info: maps to hal_bmc.HalBmc.get_info, returns version, current_boot, next_boot
       GET:
       Request param: None
       Response.json():
       {
           "status": "OK",
           "message": "OK",
           "data": {
               "Version": "1.2.3",
               "Flash": "master",
               "Next": "master"
           }
       }

   1.2 /api/bmc/versions: maps to hal_bmc.HalBmc.get_version_all, returns master+slave version
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Master": "1.2.3",
               "Slave": "1.1.0"
           }
       }

   1.3 /api/bmc/status: maps to hal_bmc.HalBmc.get_status, returns status of CPU/Memory/Disk
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               # "N/A" for invalid outpouts
                {
                    "CPU": {
                        "StateOutputs": "output of command 'top -bn 1'"
                        "Usage": "10.0"
                    },
                    "MEMORY": {
                        "StateOutputs": "output of command 'free -m'"
                        "Usage": "15.0"
                    },
                    "DISK": {
                        "StateOutput": "output of command 'df -h'"
                        "Usage": "12.5"
                    }
                }
           }
       }

   1.4 /api/bmc/nextboot: maps to hal_bmc.HalBmc.get/set_next_boot, get/set next boot flash
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Flash": "slave"
           }
       }

       POST:
       Request param:
       {
           "Flash": "master"  # or "slave"
       }
       Response.json(): check "NOTE" section below

   1.5 /api/bmc/reboot: maps to hal_bmc.HalBmc.reboot
       POST:
       Request param: None
       Response.json(): check "NOTE" section below

2. Fan
   2.1 /api/fan/info: maps to hal_fan.HalFan.get_info_all, returns all fans’ FRU info and status
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               # Content of fan_dict, defined by hal_fan.HalFan.get_info_all
           }
       }

   2.2 /api/fan/number: maps to hal_fan.HalFan.get_total_number, returns platform total fan count
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Number": 4
           }
       }

3. PSU
   3.1 /api/psu/info: maps to hal_psu.HalPsu.get_info_all, returns all PSU’s FRU info and status
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               # Content of fan_dict, defined by hal_psu.HalPsu.get_info_all
           }
       }

   3.2 /api/psu/number: maps to hal_psu.HalPsu.get_total_number, returns platform total psu count
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Number": 2
           }
       }

4. Sensor
   4.1 /api/sensor/info: maps to hal_sensor.HalSensor.get_sensor_info, returns all sensors name, value, range
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               # Content of fan_dict, defined by hal_sensor.HalSensor.get_sensor_info
           }
       }

5. Firmware
   5.1 /api/firmware/upgrade: maps to hal_firmware.HalFirmware.program_bios/bmc/cpld
       POST:
       Request param:
       {
           "Name": "bios"    # or "bmc"
           "Flash": "master" # "slave" or "both"
           "Path": "path of image in bmc"
       }
       Response.json(): check "NOTE" section below

   5.2 /api/firmware/biosnextboot: maps to hal_firmware.HalFirmware.get/set_bios_next_boot
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Flash": "master"
           }
       }
       POST:
       Request param:
       {
           "Flash": "master"    # or "slave"
       }
       Response.json(): check "NOTE" section below

       Note: for bios, "master"/"slave" stands for "primary"/"secondary"

   5.3 /api/firmware/refresh: maps to hal_firmware.HalFirmware.refresh
       POST:
       Request param:
       {
           "Names": ["base_cpld", "fan_cpld", "fpga", "bios"]
           "Paths": ["/tmp/base_cpld_refresh.vme", "/tmp/fan_cpld_refresh.vme", "none", "none"]
       }
       Response.json(): check "NOTE" section below

   5.4 /api/firmware/cpldversion: maps to hal_misc.HalMisc.get_cpld_version
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "FAN_CPLD": "0.1",     # or "N/A" for read failure
               "BASE_CPLD": "0.2"
           }
       }

   5.5 /api/misc/biosbootstatus: map to hal_misc.HalMisc.get_bios_boot_status
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Flash": "master",
               "Result": "success"
           }
       }

6. Arbitrary commands
   6.1 /api/hw/rawcmd
       POST:
       Request param:
       {
           "Command": "command string with parameters"
       }
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Outputs": "outputs of the command"
           }
       }

   6.2 /api/hw/powercycle: power cycle CPU(and affilliates) or the whole system
       POST:
       Request param:
       {
           "Entity": "cpu"    # or "system"
       }
       Response.json(): check "NOTE" section below

   6.3 /api/hw/locationled: maps to hal_misc.HalMisc.set/get_location_led
       GET:
       Request param: None
       Response.json():
       {
           # "status" and "message", both be "OK"
           "data": {
               "Status": "off"
           }
       }
       POST:
       Request param:
       {
           "Command": "on"
       }
       Response.json(): check "NOTE" section below

Note:
    For a failed request(GET and POST), response.json() should be:
    {
        "status": "ERROR",
        "messages": "Detailed message for the failure",
        "data": {}    # Empty
    }

    For a POST request, successful response.json() should be:
    {
        "status": "OK",
        "messages": "OK"
        "data": {}
    }

