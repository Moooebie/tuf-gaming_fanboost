#!/usr/bin/python3
import os
import sys

def stat():
	print('Status: ', end='')
	status = os.popen(r'cat /sys/class/hwmon/hwmon5/device/fan_boost_mode').read()
	if(status=='0\n'):
		print('DISABLED')
	elif(status=='1\n'):
		print('ENABLED')
	else:
		print('UNKNOWN STATUS!\n\t', status)


def help():
	print ("""Fan_Boost_Mode Controller for ASUS TUF GAMING Laptops.
Version 1.0
By Moebie Wu

Usage:	fanboost [subcommand]
	fanboost [-h|--help]

Available Options:
  -h --help	Show this help information.

Available Subcommands:
  help		As above.
  on		Enable Fan Boost Mode.
  off		Disable Fan Boost Mode.
  status	Show the status of Fan Noost Mode.
	""")

if(len(sys.argv)==2):
	arg = sys.argv[1]

else:
	help()
	quit()

if (arg=='status'):
	stat()

elif (arg=='on'):
	print('Turning on fan_boost_mode...')
	os.system(r'sudo bash -c "echo 1 > /sys/class/hwmon/hwmon5/device/fan_boost_mode"')
	stat()

elif (arg=='off'):
	print('Turning off fan_boost_mode...')
	os.system(r'sudo bash -c "echo 0 > /sys/class/hwmon/hwmon5/device/fan_boost_mode"')
	stat()

elif (arg=='help' or arg=='--help' or arg=='-h'):
	help()

else:
	print('Invalid argument(s). Use "fanboost --help" for usage.\n')
	help()
