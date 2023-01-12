#!/usr/bin/env python3

######################################################
#                   Case_Notes.py                    #
#                  BETA Version 0.3                  #
#----------------------------------------------------#
#           Written by: John G. Asmussen             #
#          EGA Technology Specialists, LLC.          #
#                   GNU GPL v 3.0                    #
######################################################

import datetime
import os
import sys
from pyautogui import hotkey

log_filename = sys.argv[1]

def write_log(log):
  timestamp = str(datetime.datetime.utcnow())
  with open(log_filename, 'a') as log_file:
    log_file.write(timestamp + "|: " + log + "\n")

if '-h' in sys.argv or '--help' in sys.argv:
  print("Case_Notes.py: a program for creating a case notes log file complete with UTC date and timestamps.")
  print('\n')
  print("Usage: python3 Case_Notes.py [NAME_OF_LOG_FILE]")
  print('\n')
  print("	[--help] or [-h] prints this message.")
  print('\n')
  print("For a new case, the user will be prompted to enter their Name, ID, and a Case Number.")
  print('\n')
  print("The program will drop the user to a persistent prompt where case notes can be entered. There are only two command options to use:")
  print('\n')
  print(" 	- Enter !s to take a screenshot.")
  print('\n')
  print(" 	- Enter !q to exit the program.")
  print('\n')
  print("The latest version of this script can be found here: https://github.com/jgasmussen/Case_Notes.py")
  sys.exit()

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
  user_input = input("Enter a note to be logged: (!q to quit)")

  if user_input == '!s':
    write_log("=============== USER TOOK A SCREENSHOT ===============")
  #Linux
    #hotkey("shift", "printscreen")
  #Windows
    hotkey("win","shift","s")
  #macOS
    #hotkey("command","shift","4")
    continue

  if user_input == '!q':
    write_log("=============== USER QUIT PROGRAM ===============")
    break

  write_log(user_input)
