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

########## GRAD PY ##############
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
cprint("DHARMESH'S GRADUATION", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S GRADUTAIONS LOADED 100%")

############# DEGREE ################
print()
cprint("BACHELORS DEGREE", 'blue', attrs=['bold'])
time.sleep(1)

words = "UNIVERSITY OF MADRAS (2010-2013)\n"
words1 = "\tLOCATION: CHENNAI, TAMILNADU, INDIA \n"
words2 = "\tFIELD: BACHELORS OF SCIENCE - COMPUTER SCIENCE\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
for char in words1:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
for char in words2:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

print()
cprint("MASTERS DEGREE", 'blue', attrs=['bold'])
time.sleep(1)

words3 = "SRM INSTITUTE OF SCIENCE AND TECHNOLOGY (2013-2016)\n"
words4 = "\tLOCATION: CHENNAI, TAMILNADU, INDIA \n"
words5 = "\tFIELD: MASTER OF COMPUTER APPLICATION (MCA)\n\n"
for char in words3:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
for char in words4:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()
for char in words5:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()