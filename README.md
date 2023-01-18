# Case_Notes.py

## Case_Notes.py is a cross-platform (Windows, macOS, & Linux) python script to help make the documentation process of the forensic examination easier.

Case_Notes.py is easy to setup and use!

A simple python script that keeps your forensic case notes organized all in one place complete with a running date and timestamp for each entry.

### NEW in VERSION 1.0 - Case_Notes.py now has a screenshot shortcut capability! 
- Case_Notes.py uses the OS's native keyboard shortcut, allowing the user to "click and drag" a specific area of the screen.
- Faster screenshots resulting in cleaner and easier to read screenshots of key pieces of evidence.
- Automatic OS detection for screenshot shortcuts. 
- Users can specify the Date/Timestamp in either UTC or local time. 

As pointed out by other users, "Case_Notes.py" can also be used for other documentation purposes: 
- Open Source Intelligence (OSINT) investigations.
- Social Media Intelligence (SOCMINT) investigations.
- Notes during penetration tests.
- Capture the Flag (CTF) events. 
- General note taking.
- And so much more!

## Installation Instructions:

1. First make sure python3 is installed and up to date.

  ``` 
  $ python3 -V
  ```

2. Make sure pip is installed.

  ```
  $ pip3 -V
  ```
  
  If pip is not installed, you will need to install it using the directions found here: 
  
  Windows: https://www.geeksforgeeks.org/how-to-install-pip-on-windows/
  
  Linux: https://www.geeksforgeeks.org/how-to-install-pip-in-linux/
  
  macOS: https://www.geeksforgeeks.org/how-to-install-pip-in-macos/

3. Using pip, install the required module: "pyautogui"

  ```
  $ pip3 install pyautogui
  ```

4. Clone this respository:

  ```
  $ git clone https://github.com/jgasmussen/Case_Notes.py
  ```

5. Finally, we need to make the script exectuable. For macOS and Linux run:

  ```
  $ chmod +x Case_Notes.py
  ```

6. In Windows, right click on the python script and select "Properties." Click the check box "Unblock" to allow it to run.

That's it! You are now ready to run the script.

Note: For macOS, you may need to give permission to the "Terminal App" in order for it to allow the screenshot functionality to work.  

## Using Case_Notes.py

First, let's run the Case_Notes.py from the command line with the help flag:

```
$ python3 Case_Notes.py --help
```

``` 
Case_Notes.py: a program for creating a case notes log file complete with UTC date and timestamps.


Usage: python3 Case_Notes.py [NAME_OF_LOG_FILE] [DATE_TIMESTAMP_FORMAT]


 [--help] or [-h] prints this message.


 [--UTC] specifies the UTC date/timestamp for the log file.


 [--LocalTime] specifies the Local Time date/timestamp for the log file.


For a new case, the user will be prompted to enter their Name, ID, and a Case Number.


The program will drop the user to a persistent prompt where case notes can be entered. There are only two command options to use:


   - Enter !s to take a screenshot.


   - Enter !q to exit the program.


The latest version of this script can be found here: https://github.com/jgasmussen/Case_Notes.py

```


## To run the program, use the following command:

```
$ python3 Case_Notes.py case_notes.log --UTC
```

You can replace "case_notes" with any filename you want.

If this is a new case, the first thing the program will do is prompt you to enter your Name, ID number, and a Case number. This information will be printed in the header of the newly created case log file.

The program will then continue and leave you at a persistent prompt where you can type your notes as needed. 
Pressing return will write the data to the log file.
Pressing "!s" will activate your OS's keyboard combination to take a selected screenshot. Using the mouse cursor, left click and drag to highlight an area of the screen and select it for a screenshot. Save the screenshot to the same directory as your case log file. 
For everytime you push "!s" the log file also includes an entry with the date/timestamp showing you took a screen.

Whenever you are finished (either for the day or for the case is complete) you exit the program using the "!q" command.
This will make a timestamped entry into the log file indiciating the User Quit the Program.

If you need to restart the investigation in the future, simply rerun the command:

```
$ python3 Case_Notes.py case_notes.log --UTC
```

Re-running the command will re-start the program where you left off and also log an entry into the log file that the user restarted the program.


That's it! If you have any ideas of features you would like added or modifications to the existing code that you want to see implementd please let me know.
