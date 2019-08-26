#!/usr/bin/env python

#import
import signal
import sys
import os
import time
from termcolor import colored, cprint #requirement.txt
from tqdm import tqdm #requirement.txt
from time import sleep


os.system('clear')

########## GLOBAL CERT PY ##############
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
cprint("DHARMESH'S CONTACTS", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S CONTACTS LOADED 100%")

############# LANGUAGES ################
print()
cprint("LIST OF CONTACTS", 'blue', attrs=['bold'])
time.sleep(1)

words = "\n1.FULL NAME: Dharmesh Baskaran\n\n2.EMAIL ID: dharmesh201093@gmail.com\n\n3.MOBILE: +919941943638\n\n4.DATE OF BIRTH: 22 March 1993\n\n5.YEARS OF EXP: 3 Years\n\n6.TWITTER: @dharmesh789\n\n7.LinkedIn: https://www.linkedin.com/in/dharmeshbaskaran\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()