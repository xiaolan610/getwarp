import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys
import multiprocessing

os.system("title WARP-PLUS-CLOUDFLARE By ALIILAPRO")
os.system('cls' if os.name == 'nt' else 'clear')
print('Getting WARP+ Traffic on Github Actions')
referrer = "c8c65ab5-2c9f-42de-ad94-64ab73531cbe"
def genString(stringLength):
	try:
		letters = string.ascii_letters + string.digits
		return ''.join(random.choice(letters) for i in range(stringLength))
	except Exception as error:
		print(error)		    
def digitString(stringLength):
	try:
		digit = string.digits
		return ''.join((random.choice(digit) for i in range(stringLength)))    
	except Exception as error:
		print(error)	
url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'
def run():
	try:
		install_id = genString(22)
		body = {"key": "{}=".format(genString(43)),
				"install_id": install_id,
				"fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
				"referrer": referrer,
				"warp_enabled": False,
				"tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
				"type": "Android",
				"locale": "es_ES"}
		data = json.dumps(body).encode('utf8')
		headers = {'Content-Type': 'application/json; charset=UTF-8',
					'Host': 'api.cloudflareclient.com',
					'Connection': 'Keep-Alive',
					'Accept-Encoding': 'gzip',
					'User-Agent': 'okhttp/3.12.1'
					}
		req         = urllib.request.Request(url, data, headers)
		response    = urllib.request.urlopen(req)
		status_code = response.getcode()	
		return status_code
	except Exception as error:
		print(error)	
def start():
	g = 0
	b = 0
	while True:
		result = run()
		if result == 200:
			g = g + 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print("")
			print("Getting WARP+ Traffic")
			print("")
			print(f"\n[-] WORK ON ID: {referrer}")    
			print(f"[:)] {g} GB has been successfully added to your account.")
			print(f"[#] Total: {g} Good {b} Bad")
			print("[*] After 5 seconds, a new request will be sent.")
			time.sleep(15)
		else:
			b = b + 1
			os.system('cls' if os.name == 'nt' else 'clear')
			print("")
			print("Getting WARP+ Traffic")
			print("")
			print("[:(] Error when connecting to server.")
			print(f"[#] Total: {g} Good {b} Bad")	
p0 = multiprocessing.Process(target=start)
p1 = multiprocessing.Process(target=start)
p2 = multiprocessing.Process(target=start)
p3 = multiprocessing.Process(target=start)
p4 = multiprocessing.Process(target=start)
p5 = multiprocessing.Process(target=start)
p6 = multiprocessing.Process(target=start)
p7 = multiprocessing.Process(target=start)
p8 = multiprocessing.Process(target=start)
p9 = multiprocessing.Process(target=start)
p10 = multiprocessing.Process(target=start)
p11 = multiprocessing.Process(target=start)
p12 = multiprocessing.Process(target=start)
p13 = multiprocessing.Process(target=start)
p14 = multiprocessing.Process(target=start)
p15 = multiprocessing.Process(target=start)
p0.start()
p0.join()
p1.start()
p1.join()
p2.start()
p2.join()
p3.start()
p3.join()
p4.start()
p4.join()
p5.start()
p5.join()
p6.start()
p6.join()
p7.start()
p7.join()
p8.start()
p8.join()
p9.start()
p9.join()
p10.start()
p10.join()
p11.start()
p11.join()
p12.start()
p12.join()
p13.start()
p13.join()
p14.start()
p14.join()
p15.start()
p15.join()
