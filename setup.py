import os, sys
import configparser
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
def banner():
	os.system('clear')
	print(f"""
	{re}╔═╗{cy}┌─┐┌┬┐┬ ┬┌─┐
	{re}╚═╗{cy}├┤  │ │ │├─┘
	{re}╚═╝{cy}└─┘ ┴ └─┘┴   v1.4
	""")
banner()
print(gr+"[+] Installing requierments ...")
os.system('python3 -m pip install telethon')
os.system('pip3 install telethon')
banner()
os.system("touch config.data")
cpass = configparser.RawConfigParser()
cpass.add_section('cred')
xid = input(gr+"[+] Enter API ID : "+re)
cpass.set('cred', 'id', xid)
xhash = input(gr+"[+] Enter Hash : "+re)
cpass.set('cred', 'hash', xhash)
xphone = input(gr+"[+] Enter Phone Number: "+re)
cpass.set('cred', 'phone', xphone)
with open('config.data', 'w') as setup:
	cpass.write(setup)
print(gr+"[+] Setup complete!")
print(gr+"[+] Now you can run any tool!")
print(gr+"[+] Make sure to read README.md before using this tool.")
print(gr+"[+] https://github.com/TharukRenuja/TelegramScraper/blob/master/README.md")
