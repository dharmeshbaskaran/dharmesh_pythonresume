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

########## LANGUAGES PY ##############
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
cprint("DHARMESH'S WELLKNOWN LANGUAGES", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S WELLKNOWN LANGUAGES LOADED 100%")

############# LANGUAGES ################
print()
cprint("WELLKNOWN LANGUAGES", 'blue', attrs=['bold'])
time.sleep(1)

words = "\n\n1.English - Full Professional Proficiency\n\n2.French - Limited Working Proficiency\n\n3.Hindi - Professional Working Proficiency\n\n4.Tamil - Professional Working Proficiency\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()