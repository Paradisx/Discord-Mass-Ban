import os, requests, threading, time
user_ids = []
white = "\x1b[0m"
pink = "\x1b[38;5;218m"

def Main():
    os.system(f'title [Auditor] By Ashley & mode 80,24 &')
    print(f'''
        \t\t{pink} ╔════════════════════════╗
        \t\t{pink} ║{pink}[{white}1{pink}]{white} Mass Ban           {pink} ║
        \t\t{pink} ║{pink}[{white}2{pink}]{white} Mass Unban         {pink} ║
        \t\t{pink} ╚════════════════════════╝{white}''')
    option = input(f"{pink}[{white}?{pink}]{white} Option{pink}?{white} ")
    if option == '1':
        token = input(f"{pink}[{white}?{pink}]{white} Token{pink}?{white} ")
        bot = input(f"{pink}[{white}?{pink}]{white} Bot[true,false]{pink}?{white} ")
        guild = input(f"{pink}[{white}?{pink}]{white} Guild ID{pink}?{white} ")
        users = open('ids.txt').readlines()
        for member in users:
            user = member.replace("\n", "")
            user_ids.append(user)
        os.system(f'cls & mode 31,24 & title [Auditor] By Ashley')
        for m in range(len(user_ids)):
            threading.Thread(target=ban, args=(token, bot, guild, user_ids[m],)).start()
        os.system("pause >NUL")
        Main()
    elif option == '2':
        token = input(f"{pink}[{white}?{pink}]{white} Token{pink}?{white} ")
        bot = input(f"{pink}[{white}?{pink}]{white} Bot[true,false]{pink}?{white} ")
        guild = input(f"{pink}[{white}?{pink}]{white} Guild ID{pink}?{white} ")
        users = open('ids.txt').readlines()
        for member in users:
            user = member.replace("\n", "")
            user_ids.append(user)
        os.system(f'cls & mode 33,24 & title [Auditor] By Ashley')
        for m in range(len(user_ids)):
            threading.Thread(target=unban, args=(token, bot, guild, user_ids[m],)).start()
        os.system("pause >NUL")
        Main()
        
def ban(token, bot, guild, i):
    if bot == "true":
        headers = {"Authorization": f"Bot {token}"}
    else:
        headers = {"Authorization": f"{token}"}
    r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",headers=headers)
    if r.status_code == 429:
        print(f"{pink}[{white}${pink}]{white} Rate Limited For {pink}[{white}{r.json()['retry_after']}{pink}]{white}")
        time.sleep(r.json()['retry_after'])
        ban(token, bot, guild, i)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{pink}[{white}${pink}]{white} Banned {pink}[{white}{i}{pink}]{white}")

def unban(token, bot, guild, i):
    if bot == "true":
        headers = {"Authorization": f"Bot {token}"}
    else:
        headers = {"Authorization": f"{token}"}
    r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/bans/{i}",headers=headers)
    if r.status_code == 429:
        print(f"{pink}[{white}${pink}]{white} Rate Limited For {pink}[{white}{r.json()['retry_after']}{pink}]{white}")
        time.sleep(r.json()['retry_after'])
        unban(token, bot, guild, i)
    elif r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        print(f"{pink}[{white}${pink}]{white} Unbanned {pink}[{white}{i}{pink}]{white}")

Main()
