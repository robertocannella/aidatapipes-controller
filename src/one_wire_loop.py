#  ************ one_wire_loop.py  ************************************ #
#                                                                      #
#  A.I. DataPipes  - 05-07-2022 - Roberto Cannella                     #
#  1-wire script which periodically fetches reading from various       #
#  1-wire devices.  This script utilizes Linux OWFS to access          #
#  primary and secondary devices                                       #
#                                                                      #
#  System Type: Forced Hot Water (PUMP)                                #
#                                                                      #                                          #
#                                                                      #
#  ******************************************************************* #


from datetime import date, datetime
import math
from services import mongodb_service as db
from services import firebase_service as fb

import os
import time
import glob
from decouple import config

base_dir = '/mnt/1wire/'

# Get all the directories that begin with 28 (DS18B20) temp family
devices = glob.glob(base_dir + '28*')
system_id = config('FB_SYSTEM_ID')


def read_raw(property_path):
    f = open(property_path, 'r')
    lines = f.readlines()
    f.close()
    return lines


def read_temp(device):
    temp_path = glob.glob(device + '/temperature12')[0]  # 12 bit resolution
    lines = read_raw(temp_path)
    temp_c = float(lines[0])
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f


def read_address(device):
    addr_path = glob.glob(device + '/address')[0]
    lines = read_raw(addr_path)
    return lines[0]


# starting zone index
zone_index = 10
for device in devices:
    device_address = read_address(device)
    deg_c, deg_f = read_temp(device)
    print(device_address)
    print(' Deg C: {0} | Deg F {1}'.format(
        "{:3.3f}".format(deg_c), "{:3.3f}".format(deg_f)))
    # print(datetime.now())
    fb.append_last_temp_reading(collection='systems', system_id='test-id',
                                document='zone', zone_index=zone_index, reading_type='lineRT', degrees_fahrenheit=deg_f)
    zone_index = zone_index + 1
    time.sleep(2)
