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

########## SKILLS PY ##############
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
cprint("DHARMESH'S AWESOME SKILLS", 'red', attrs=['blink','bold'])
time.sleep(1)

############ LOADING EFFECT #############
for x in tqdm(range(100)):
	time.sleep(0.01)
print()
print("WOW DHARMESH'S SKILLS LOADED 100%")


############# CORE SKILL ################
print()
cprint("CORE SKILLS", 'blue', attrs=['bold'])
time.sleep(1)


words = "1.Web Application Security (SAST / DAST)\n\n2.Mobile Application Security (Android and iOS)(Fuzzing / Reverse Engineering)\n\n3.Source Code Review (Static Analysis)\n\n4.Network Security (Vulnerablity Assessment and Penetration Testing)\n\n5.PCI-DSS (Auditing / Implementation)\n\n6.ISO 27001:2015 Auditing\n\n7.DevOps / DevSecOps Tools (Docker, Jenkins, Dagda)\n\n8.Cloud Technology (Azure - Creating VM's, Maintain resource group, Secuirty Management)\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()

############# TECHNICAL SKILLS #####################

print()
cprint("SOME TECHNICAL SKILLS BASED ON CORE SKILLS", 'blue', attrs=['bold'])
time.sleep(1)

words = "1.OWASP MOBILE TOP 10 (2016)\n\n2.OWASP TOP 10 WEB APPLICATION (2017)\n\n3.CCNA ROUTING AND SWITCHING\n\tTRAINED (Router / Switch / Firewall Configuration)\n\n4.CCNA SECURITY\n\tTRAINED (Firewall Rules, Port Security, Firewall Configuration)\n\n5.OPERATING SYSTEMS\n\tWindows 7 (As Vulnerable OS To Test Metasploit)\n\tWindows 8.1/10(Mostly Windows Based Hacking and World of Warcraft Gaming)\n\tMAC OS X - (Sierra/High Sierra/Mojave) (I Use This OS Personally, Mostly Mobile Security and Logic Pro X to Produce Music)\n\tLINUX - Debian,RPM (I Use This For Hacking and Coding and also I use this as Professional)\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()


############## SCRIPTING LANGUAGE SKILLS ################

print()
cprint("SCRIPTING SKILLS", 'blue', attrs=['bold'])
time.sleep(1)

words = "1.BASH SCRIPTING\n\tTOOL DEVELOPMENT / AUTOMATION\n\n2.PYTHON\n\tTOOL DEVELOPMENT / AUTOMATION / MACHINE LEARNING\n\n3.JAVA SCRIPT, C#, HTML\n\tMOBILE SECURITY - Android and iOS (Fuzzing / Reverse Engineering)\n\tWEB APPLICATION SECURITY\n\tSTATIC SOURCECODE REVIEW\n\n"
for char in words:
    sleep(0.02)
    sys.stdout.write(char)
    sys.stdout.flush()