import requests
import queue
import threading
##https://free-proxy-list.net

q= queue.Queue()
valid_proxies=[]

with open("proxy_list.txt","r")as f:
	proxies= f.read().split("\n")
	for p in proxies:
		q.put(p)


def check_proxies():
	global q
	while not q.empty():
		proxy = q.get()
		try:
			res = requests.get("http://ipinfo.io/json",proxies={"http":proxy,"https":proxy})

		except Exception as e:
			continue
		if res.status_code == 200:
			print(proxy)


for t in range(10):
	threading.Thread(target=check_proxies).start()
