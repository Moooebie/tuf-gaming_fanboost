#!/usr/bin/python3
import os
import sys

# Path of the fan_boost_mode config
path = r'/sys/devices/platform/asus-nb-wmi/fan_boost_mode'
try:
	f=open(path, mode='r')
except FileNotFoundError:
	print('Config file "', path, '" does not exist!', sep='')
	sys.exit(1)
finally:
	f.close()

def stat():
	print('Path:', path, sep='\t')
	print('Status:\t', end='')
	status = os.popen(f'cat {path}').read()
	if(status=='0\n'):
		print('DISABLED')
	elif(status=='1\n'):
		print('ENABLED')
	else:
		print('UNKNOWN STATUS! [', status, ']', sep='')


def help():
	print ("""Fan_Boost_Mode Controller for ASUS TUF GAMING Laptops.
Version 1.1
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
	sys.exit(0)

if (arg=='status'):
	stat()
elif (arg=='on'):
	print('Turning on fan_boost_mode...')
	os.system(f'sudo bash -c "echo 1 > {path}"')
	stat()
elif (arg=='off'):
	print('Turning off fan_boost_mode...')
	os.system(f'sudo bash -c "echo 0 > {path}"')
	stat()
elif (arg=='help' or arg=='--help' or arg=='-h'):
	help()
else:
	print('Invalid argument(s). Use "fanboost --help" for usage.\n')
	help()
