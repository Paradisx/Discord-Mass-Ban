import os, threading, time, requests

class color():
	PINK = '\x1b[38;5;207m'
	WHITE = '\033[39m'

user_ids = []

def Main(): 
    os.system(f'title [Mass Ban] By Dassidy')
    print(f'''
        {color.PINK} ╔════════════════════════╗
        {color.PINK} ║{color.PINK}[{color.WHITE}1{color.PINK}]{color.WHITE} Mass Ban           {color.PINK} ║
        {color.PINK} ║{color.PINK}[{color.WHITE}2{color.PINK}]{color.WHITE} Mass Unban         {color.PINK} ║
        {color.PINK} ╚════════════════════════╝''')
    option = input(color.PINK + '> ' + color.WHITE)
    if option == '1':
        guild = input(f"{color.PINK}[{color.WHITE}?{color.PINK}]{color.WHITE} Guild ID{color.PINK}>{color.WHITE} ")
        token = input(f"{color.PINK}[{color.WHITE}?{color.PINK}]{color.WHITE} Token{color.PINK}>{color.WHITE} ")
        users = open('ids.txt').readlines()
        for member in users:
            user = member.replace("\n", "")
            user_ids.append(user)
        for m in range(len(user_ids)):
            threading.Thread(target=ban, args=(guild, token,user_ids[m],)).start()
        time.sleep(4)
        clear()
        Main()
    elif option == '2':
        guild = input(f"{color.PINK}[{color.WHITE}?{color.PINK}]{color.WHITE} Guild ID{color.PINK}>{color.WHITE} ")
        token = input(f"{color.PINK}[{color.WHITE}?{color.PINK}]{color.WHITE} Token{color.PINK}>{color.WHITE} ")
        users = open('ids.txt').readlines()
        for member in users:
            user = member.replace("\n", "")
            user_ids.append(user)
        for m in range(len(user_ids)):
            threading.Thread(target=ban, args=(guild, token,user_ids[m],)).start()
        time.sleep(4)
        clear()
        Main()

def ban(guild, token, i):
    headers = {'Authorization': f'{token}'}
    r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}",headers=headers)
    if r.status_code == 429:
        print(f"{color.PINK}[{color.WHITE}Lunar Banner{color.PINK}]{color.WHITE} Rate Limited For {color.PINK}[{color.WHITE}{r.json()['retry_after']}{color.PINK}]{color.WHITE}")
        time.sleep(r.json()['retry_after'])
        ban(guild, token, i)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{color.PINK}[{color.WHITE}Lunar Banner{color.PINK}]{color.WHITE} Banned {color.PINK}[{color.WHITE}{i}{color.PINK}]{color.WHITE}")

def unban(guild, token, i):
    headers = {'Authorization': f'{token}'}
    r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}",headers=headers)
    if r.status_code == 429:
        print(f"{color.PINK}[{color.WHITE}Lunar UnBanner{color.PINK}]{color.WHITE} Rate Limited For {color.PINK}[{color.WHITE}{r.json()['retry_after']}{color.PINK}]{color.WHITE}")
        time.sleep(r.json()['retry_after'])
        unban(guild, token, i)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{color.PINK}[{color.WHITE}Lunar UnBanner{color.PINK}]{color.WHITE} UnBanned {color.PINK}[{color.WHITE}{i}{color.PINK}]{color.WHITE}")

Main()
