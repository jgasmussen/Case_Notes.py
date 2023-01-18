#!/usr/bin/env python3

######################################################
#                   Case_Notes.py                    #
#                    Version 1.0                     #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#          EGA Technology Specialists, LLC.          #
#                   GNU GPL v 3.0                    #
######################################################

import datetime
import os
import sys
import platform
from pyautogui import hotkey

log_filename = sys.argv[1] + '.log'

if '-h' in sys.argv[1] or '--help' in sys.argv[1]:
  print("Case_Notes.py: a program for creating a case notes log file complete with UTC date and timestamps.")
  print('\n')
  print("Usage: python3 Case_Notes.py [NAME_OF_LOG_FILE] [DATE_TIMESTAMP_FORMAT]")
  print('\n')
  print(" [--help] or [-h] prints this message.")
  print('\n')
  print(" [--UTC] specifies the UTC date/timestamp for the log file.")
  print('\n')
  print(" [--LocalTime] specifies the Local Time date/timestamp for the log file.")
  print('\n')
  print("For a new case, the user will be prompted to enter their Name, ID, and a Case Number.")
  print('\n')
  print("The program will drop the user to a persistent prompt where case notes can be entered. There are only two command options to use:")
  print('\n')
  print("   - Enter !s to take a screenshot.")
  print('\n')
  print("   - Enter !q to exit the program.")
  print('\n')
  print("The latest version of this script can be found here: https://github.com/jgasmussen/Case_Notes.py")
  sys.exit()

def write_log(log):
  with open(log_filename, 'a') as log_file:
    if '--UTC' in sys.argv[2]:
      log_file.write(str(datetime.datetime.utcnow()) + "(UTC Time) |: " + log + "\n")

    if '--LocalTime' in sys.argv[2]:
      log_file.write(str(datetime.datetime.now()) + "(LocalTime) |: " + log + "\n")

if os.path.exists(log_filename):
  write_log("=============== USER RESTARTED PROGRAM ===============")

if not os.path.exists(log_filename):
  examiner_name = input("Enter Examiner's name: ")
  examiner_id = input("Enter Examiner's ID#: ")
  case_number = input("Enter Case#: ")
  header = "Examiner's name: " + examiner_name + "\n" + "Examiner's ID#: " + examiner_id + "\n" + "Case#: " + case_number + "\n" + "\n"
  with open(log_filename, 'w') as log_file:
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
