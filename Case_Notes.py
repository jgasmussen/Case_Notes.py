#!/usr/bin/env python3

######################################################
#                   Case_Notes.py                    #
#                    Version 1.2                     #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#          EGA Technology Specialists, LLC.          #
#                   GNU GPL v 3.0                    #
######################################################

# A big thank you to "Pir00t" (https://github.com/Pir00t) for his contributions to this project!

import argparse
import datetime
import os
import platform
import sys
from pyautogui import hotkey

def write_log(fname, log, tformat):
	with open(f'{fname}.log', 'a') as log_file:
		if tformat == 'UTC':
			log_file.write(str(datetime.datetime.utcnow()) + f'(UTC Time) |: {log}\n')

		if tformat == 'localtime':
			log_file.write(str(datetime.datetime.now()) + f'(LocalTime) |: {log}\n')

def main():
	parser = argparse.ArgumentParser(description = 'Case_Notes.py is a cross-platform (Windows, macOS, & Linux) python script to help make the documentation process easier.', epilog = 'The latest version of this script can be found here: https://github.com/jgasmussen/Case_Notes.py')
	parser.add_argument('-f', '--filename', metavar='', required=True, action='store', help='user specified name of the log file.')
	parser.add_argument('-t', '--time', choices=['UTC', 'localtime'], metavar='', required=True, action='store', help='log file date/time format - must choose either "UTC" or "localtime".')
	args = parser.parse_args()

	if os.path.exists(f'{args.filename}.log'): 
		write_log(args.filename, f'{"="*15} USER RESTARTED PROGRAM {"="*15}', args.time)

	if not os.path.exists(f'{args.filename}.log'):
		agency_company = input('Enter Agency / Company name: ')
		examiner_name = input('Enter Examiner name: ')
		examiner_id = input('Enter Examiner ID#: ')
		case_number = input('Enter Case#: ')
		header = f'Agency / Company name: {agency_company}\nExaminer name: {examiner_name}\nExaminer ID#: {examiner_id}\nCase#: {case_number}\n\n'
		with open(f'{args.filename}.log', 'w') as log_file:
			log_file.write(header)

	while True:
		user_input = input('Enter a note to be logged: (!q to quit) ')

		if user_input == '!s':
			write_log(args.filename, f'{"="*15} USER TOOK A SCREENSHOT {"="*15}', args.time)

			if platform.system() == 'Linux':
				hotkey('shift', 'printscreen')

			if platform.system() == 'Windows':
				hotkey('win','shift','s')

			if platform.system() == 'Darwin':
				hotkey('command','shift','4')

			continue

		elif user_input == '!q':
			write_log(args.filename, f'{"="*15} USER QUIT PROGRAM {"="*15}', args.time)
			break
	
		elif user_input == '!m':
			lines = []
			print('Submit multi-line input & type "done" when complete')
			while True:
				line = input()
				if line == 'done':
					break
				else:
					lines.append(line)
			
			lines_fmt = '\n' + '\n'.join(lines)
			write_log(args.filename, lines_fmt, args.time)

		else:
			write_log(args.filename, user_input, args.time)
	
if __name__ == '__main__':
	main()
