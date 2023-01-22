#!/usr/bin/env python3

######################################################
#                   Case_Notes.py                    #
#                    Version 1.1                     #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#          EGA Technology Specialists, LLC.          #
#                   GNU GPL v 3.0                    #
######################################################

import argparse
import datetime
import os
import platform
import sys
from pyautogui import hotkey

parser = argparse.ArgumentParser(description = "Case_Notes.py is a cross-platform (Windows, macOS, & Linux) python script to help make the documentation process easier.", epilog = "The latest version of this script can be found here: https://github.com/jgasmussen/Case_Notes.py")
parser.add_argument("-f", "--filename", metavar="", required=True, action="store", help="user specified name of the log file.")
parser.add_argument("-t", "--time", choices=['UTC', 'localtime'], metavar="", required=True, action="store", help="log file date/time format - must choose either 'UTC' or 'localtime'.")
args = parser.parse_args()

def write_log(log):
  with open(args.filename + '.log', 'a') as log_file:
    if args.time == 'UTC':
      log_file.write(str(datetime.datetime.utcnow()) + "(UTC Time) |: " + log + "\n")

    if args.time == 'localtime':
      log_file.write(str(datetime.datetime.now()) + "(LocalTime) |: " + log + "\n")

if os.path.exists(args.filename + '.log'): 
  write_log("=============== USER RESTARTED PROGRAM ===============")

if not os.path.exists(args.filename + '.log'):
  agency_company = input("Enter Agency / Company name: ")
  examiner_name = input("Enter Examiner's name: ")
  examiner_id = input("Enter Examiner's ID#: ")
  case_number = input("Enter Case#: ")
  header = "Agency / Company name: " + agency_company + "\n" + "Examiner's name: " + examiner_name + "\n" + "Examiner's ID#: " + examiner_id + "\n" + "Case#: " + case_number + "\n" + "\n"
  with open(args.filename + '.log', 'w') as log_file:
    log_file.write(header)

while True:
  user_input = input("Enter a note to be logged: (!q to quit) ")

  if user_input == '!s':
    write_log("=============== USER TOOK A SCREENSHOT ===============")

    if platform.system() == 'Linux':
      hotkey("shift", "printscreen")

    if platform.system() == 'Windows':
      hotkey("win","shift","s")

    if platform.system() == 'Darwin':
      hotkey("command","shift","4")

    continue

  if user_input == '!q':
    write_log("=============== USER QUIT PROGRAM ===============")
    break

  write_log(user_input)
