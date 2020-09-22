import requests
import services

# Adding some colours into it :)
green     = '\033[92m'
cyan      = '\033[95m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

# Making myself immortal
print(f"{green}{bold}\t\t{underline}[RUSSIAN BOMBER BY NANDYDARK :) ]{end}")

print()
print(f"{bold}Made By{end}", end="")
print(f"{green}{bold} -> {end}", end="")
print(f"{cyan}{bold}NANDYDARK{end}")

print("███    ██  █████  ███    ██ ██████  ██    ██ ██████   █████  ██████  ██   ██ ")
print("████   ██ ██  ██  ████   ██ ██   ██  ██  ██  ██   ██ ██   ██ ██   ██ ██  ██  ")
print("██ ██  ██ ███████ ██ ██  ██ ██   ██   ████   ██   ██ ███████ ██████  █████   ")
print("██  ██ ██ ██   ██ ██  ██ ██ ██   ██    ██    ██   ██ ██   ██ ██   ██ ██  ██  ")
print("██   ████ ██   ██ ██   ████ ██████     ██    ██████  ██   ██ ██   ██ ██   ██")

print(f"{bold}GITHUB{end}", end="")
print(f"{green}{bold} -> {end}", end="")
print(f"{cyan}{bold}www.github.com/nandydark{end}")
print()

# inputs
print("Enter The Number Without + Or Any Brackets\nExample Put In This Way: 8018575565")
input_number = input(green + bold + "->" + end)
print("How many messages you want to send? (maxm is 9999999999999999999999999999999999999999999)")
sms = int(input(green + bold + "->" + end))


def parse_number(number):
	msg = f"[*]check number - {green}{bold}OK{end}"
	if len(number) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]check number - {red}{bold}failed number!{end}\nThis tool currently works for Russian Number only..But i am working on a new tool that will work on any country..So stay tuned with me and follow me on my Github")
		quit()
	return number
number = parse_number(input_number)
# This tool is made by nandydark and if you will steal my code without my credits then you are the biggest gay on this universe :)
services.attack(number, sms)
