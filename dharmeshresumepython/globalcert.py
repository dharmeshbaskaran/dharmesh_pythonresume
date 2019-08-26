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
cprint("DHARMESH'S GLOBAL CERTIFICATIONS", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S GLOBAL CERTIFICATIONS LOADED 100%")

############# CERTIFICATIONS ################
print()
cprint("GLOBAL CERTIFICATIONS", 'blue', attrs=['bold'])
time.sleep(1)

words = "1.CEHv9 - Certified Ethical Hacker\n\tCertified by: EC-Council\n\tLicense:ECC78182137804\n\n2.ECSAv9 - EC-Council Certified Security Analyst\n\tCertified by: EC-Council\n\tLicense:ECC53907890468\n\n3.Machine Learning\n\tCertified by: Coursera | Stanford University Online\n\tLicense:G8LXH2KZ5WL8\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()