import os
import time
import glob

base_dir = '/mnt/1wire/'
# Get all the directories that begin with 28 (DS18B20) temp family
devices = glob.glob(base_dir + '28*')

def read_raw(property_path):
    f = open (property_path,'r')
    lines = f.readlines()
    f.close()
    return lines
	
def read_temp(device):
    temp_path = glob.glob(device + '/temperature12')[0]
    lines = read_raw(temp_path)
    temp_c = float(lines[0])
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f

def read_address(device):
    addr_path = glob.glob(device + '/address')[0]
    lines = read_raw(addr_path)
    return lines[0]
#def main():
#	device = "/mnt/1wire/"
#	print('Device Found')
#	print('Address: ' + sensor.address)
#	print('Family: ' + sensor.family)
#	print('ID: ' + sensor.id)
while True:
	for device in devices:
		device_address = read_address(device)
		c,f = read_temp(device)
		print(device_address)
		print(' Deg C: {0} | Deg F {1}'.format("{:3.3f}".format(c),"{:3.3f}".format(f)))
		time.sleep(0.5)
	time.sleep(1)
	print('-----------')

