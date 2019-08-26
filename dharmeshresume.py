#!/usr/bin/env python

#import
import signal
import sys
import os
import time
from termcolor import colored, cprint #requirement.txt


############# READY CHECK ##############
os.system("clear")


print()
cprint("WELCOME TO DHARMESH RESUME v1.0 - Release August 2019", 'red', attrs=['blink','bold'])
time.sleep(1)

print()
print(" [!] [LOADING DHARMESH RESUME] ")
time.sleep(3)
print(" [x] [WELL GIVE ME SOMETIME TO LOAD DHARMESH RESUME]")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [OH GOD! PLEASE GIVE ME SOME MORE TIME TO LOAD HIS RESUME]")
time.sleep(2)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [DAMN! HIS RESUME HAS GOT SO MANY CONTENTS. PLEASE BE PATIENT FOR ME TO LOAD THEM]")
time.sleep(2)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [.] ")
time.sleep(1)
print(" [x] [YEAH! ALMOST OVER LOADING IT]")
time.sleep(2)
print(" [x] [OK! 99% LOADED]")
time.sleep(2)
print(" [x] [.] ")
time.sleep(1)
print(" [✔] [UFF! FINALLY LOADED. ENJOY AND HAVE FUN.]")
time.sleep(4) 



os.system("clear")

########### BLINKING HEADING ###################
def banner():
	cprint('DHARMESH RESUME v1.0 - Release August 2019 ', 'red', attrs=['blink','bold'])
	cprint('PDF and DOCS FORMAT RESUME IS FOR KIDS', 'red', attrs=['blink','bold'])
	cprint('WITH <3 FROM DHARMESH ', 'red', attrs=['blink','bold'])

################ MAIN MENU ####################

def myresume():
	print("""
	[1] HIS AWESOME SKILLS? THEN PRESS 1

	[2] HIS GLOBAL CERTIFICATIONS? THEN PRESS 2

	[3] HIS COOL ACHEVEMENTS? THEN PRESS 3

	[4] HIS AWESOME CAREER EXPERIENCE? THEN PRESS 4

	[5] HIS GRADUATIONS? THEN PRESS 5

	[6] THE LANGUAGES HE KNOWS? THEN PRESS 6

	[7] HIS CONTACT DETAILS & ABOUT HIM? THEN PRESS 7

	[8] EXIT? OKAY! THEN PRESS 8""")




while True:
	try:
		banner()
		myresume()
		print()
		resume1=(int(input("WHAT WOULD YOU LIKE TO KNOW ABOUT DHARMESH?:")))
		if resume1 == 1:
			os.system('clear')
			os.system("python3 dharmeshresumepython/skills.py")
			continue
		elif resume1 == 2:
			os.system('clear')
			os.system("python3 dharmeshresumepython/globalcert.py")
			continue
		elif resume1 == 3:
			os.system('clear')
			os.system("python3 dharmeshresumepython/achievements.py")
			continue
		elif resume1 == 4:
			os.system('clear')
			os.system("python3 dharmeshresumepython/career.py")
			continue
		elif resume1 == 5:
			os.system('clear')
			os.system("python3 dharmeshresumepython/graduation.py")
			continue
		elif resume1 == 6:
			os.system('clear')
			os.system("python3 dharmeshresumepython/language.py")
			continue
		elif resume1 == 7:
			os.system('clear')
			os.system("python3 dharmeshresumepython/contacts.py")
			continue			
		elif resume1 == 8:
			os.system("clear")
			print("HOPE YOU ENJOYED WITH MY PYTHON RESUME. HAVE A GREAT DAY =)")
			time.sleep(1)
			exit()
		while resume1 > 8:
			os.system('clear')
			print("[!] THAT OPTION ISN'T AVAILABLE :(. PLEASE CHOOSE THE AVAILABLE OPTIONS.")
			time.sleep(1)
			break
		while resume1 == 0:
			os.system('clear')
			print("[!] THAT OPTION ISN'T AVAILABLE :(. PLEASE CHOOSE THE AVAILABLE OPTIONS.")
			time.sleep(1)
			break
	except ValueError:
		os.system("clear")
		print("[!] PLEASE ENTER THE VALID NUMBER GIVEN")
		while ValueError is True:
			banner()
			myresume()
			print()
			resume1=(int(input("WHAT WOULD YOU LIKE TO KNOW ABOUT DHARMESH?:")))