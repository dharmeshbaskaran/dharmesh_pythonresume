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

########## ACHIEVEMENTS PY ##############
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
cprint("DHARMESH'S ACHIEVEMENTS", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S ACHIEVEMENTS LOADED 100%")

############# CERTIFICATIONS ################
print()
cprint("HALL OF FAME", 'blue', attrs=['bold'])
time.sleep(1)

words = " Microsoft - Host Header Injection Vulnerability\n\tReward: Hall of Fame @ March 2018\n\tLink:https://technet.microsoft.com/en-in/security/cc308575#0318\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
