#Script_@toolsbot!py tr_

from selenium import webdriver as wb
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time, requests, mechanize, os, pyperclip, random
from googletrans import Translator
#----------------[Memilah data]----------------# 
z=0
options = Options()
options.profile = "/root/.mozilla/firefox/uce6gjdu.Oskhar"
options.headless = False
service = Service('/usr/local/bin/geckodriver')
translator = Translator()
x1="┼"
x2="─"
x3="┌┬┤"
x4="└┬┘"
x5="├┤"
x6="├┬┐"
x7="│"
hari=("Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu")
infowaktu= time.localtime()
hari_ini=hari[infowaktu[6]]
tgl=infowaktu[2]
bl=infowaktu[1]
th=infowaktu[0]
lis=["Morning","Noon","Evening","Night"]
file = open("BigData.txt","r")
daftar_nama = open("DataNama.txt","r")
tambah_daftar_nama = open("DataNama.txt","a")
daftar_nama = daftar_nama.read()
daftar_nama = daftar_nama.split("//\n")
daftar_nama1 = daftar_nama[0].split("\n\n")
daftar_nama2 = daftar_nama[1].split("\n")
daftar_nama3 = daftar_nama1[1].split(";")
DataBase = file.read()
data = DataBase.split("//\n")
BigData1 = data[0].split("\n\n")
BigData2 = data[1].split("\n")
BigData3 = data[2].split("\n\n")
BigData4 = data[3].split("\n\n")
BigData5 = data[4]
list_nama_anggota = ["Oskhar"]
try:
	BigData6 = data[5].split("\n")
except:
	BigData6 = 0
aksi_univers = BigData2[0]
reaksi_univers = BigData2[1]
reaksi_univers = reaksi_univers.split(";")
a = 0
b = 0
z = 0
nama_pengirim_pesan= ""
ttk=5

#----------------[Memberi aksi dan mengambil keputusan]----------------# 
d=wb.Firefox(options=options, service=service)
d.get("https://web.whatsapp.com")
while True:
	try:
		d.find_element_by_xpath('//span[@title="Oskhar"]').click()
		break
	except:
		z+=1
while True:
	alamatnya_xpath=d.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
	zzzz=1
	try:
		element = d.find_element_by_xpath('//div[@class="tSmQ1"]')
		pesan = element.text
		pop=""
		for Pesan in pesan.split("\n"):
			try:
				dua_titik=Pesan[2]
			except:
				dua_titik=""
				z+=0
			if str(dua_titik)==":":
				pop=pop+"///"
			else:
				pop=pop+str(Pesan)+"]]"
		pop=pop.split("///")
		pop=pop[-2]
		try:
			pop=pop.replace("TODAY","")
		except:
			z+=0
		pop=pop.split("]]")
		o=""
		for nama_anggota in list_nama_anggota:
			if zzzz==1:
				if nama_anggota == str(pop[0]):
					nama_pengirim_pesan=nama_anggota
					for i in range(len(pop)-1):
						o=o+str(pop[i+1])
					zzzz=0
		if zzzz==1:
			for i in range(len(pop)):
				o=o+str(pop[i])
		k=o.split(" ")
	except:
		z+=0
		o=""
		k=["pzp", "pzp"]

	if k[0]=="#hitung":
		try:
			bals=eval(k[1])
			ll=1
		except:
			alamatnya_xpath.send_keys("perhitungannya mana tolol?")
			alamatnya_xpath.send_keys(Keys.ENTER)
			ll=0
		if ll==1:
			ll=0
			alamatnya_xpath.send_keys(bals)
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#copy":
		try:
			pl=open("/root/Pictures/"+k[2]+".html","w")
			ll=1
		except:
			alamatnya_xpath.send_keys("Nama filenya mana tolol?")
			alamatnya_xpath.send_keys(Keys.ENTER)
			ll=0
		if ll==1:
			pl.write("")
			pl=open("/root/Pictures/"+k[2]+".html","a")
			try:
				req=requests.get(k[1])
				html=BeautifulSoup(req.text,"html.parser")
				pl.write(str(html))
				ll=2
			except:
				alamatnya_xpath.send_keys("harus menggunakan https:// atau http:// tolol")
				alamatnya_xpath.send_keys(Keys.ENTER)
			if ll==2:
				ll=0
				pyperclip.copy(str(html))
				alamatnya_xpath.send_keys(Keys.CONTROL+"v")
				alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#wiki":
		try:
			req=requests.get("https://en.wikipedia.org/wiki/"+k[1])
			ll=1
		except:
			ll=0
		if ll==1:
			ll=0
			html=BeautifulSoup(req.text,"html.parser")
			zz=html.find("body")
			zz=zz.text
			pyperclip.copy(str(zz))
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#ip":
		try:
			os.system("uniscan -u "+k[1]+" | grep IP -i>3.txt")
			ll=1
		except:
			alamatnya_xpath.send_keys("URLnya mana tolol?")
			alamatnya_xpath.send_keys(Keys.ENTER)
			ll=0
		if ll==1:
			ll=0
			opn=open("3.txt","r")
			ip=opn.read()
			alamatnya_xpath.send_keys(ip)
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#help":
			text = open("help.txt","r")
			text=text.read()
			pyperclip.copy(str(text))
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#pass":
		try:
			os.system("grep -a "+k[1]+" /root/Documents/0.0.0.0.1.txt > /root/"+k[1]+".txt")
			ll=1
		except:
			alamatnya_xpath.send_keys("key wordnya mana tolol?")
			alamatnya_xpath.send_keys(Keys.ENTER)
			ll=0
		if ll==1:
			zz=open(k[1]+".txt","r")
			zz=zz.read()
			pyperclip.copy(str(zz))
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#tr_id":
		hj=0
		for i in k:
			hj+=1
		xx=""
		for i in range(hj-1):
			xx=str(xx)+" "+str(k[i+1])
		result = translator.translate(xx, src='en', dest='id')
		pyperclip.copy(str(result.text))
		alamatnya_xpath.send_keys(Keys.CONTROL+"v")
		alamatnya_xpath.send_keys(Keys.ENTER)
		hj=0

	elif k[0]=="#tr_en":
		hj=0
		for i in k:
			hj+=1
		xx=""
		for i in range(hj-1):
			xx+=" "+str(k[i+1])
		result = translator.translate(xx, src='id', dest='en')
		pyperclip.copy(str(result.text))
		alamatnya_xpath.send_keys(Keys.CONTROL+"v")
		alamatnya_xpath.send_keys(Keys.ENTER)
		hj=0

	elif k[0]=="#kick":
		alamatnya_xpath.send_keys("lu siapa gw tolol nyuruh nyuruh gw?")
		alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#sticker":
		alamatnya_xpath.send_keys("sticker? lu siapa gw tolol nyuruh nyuruh gw?")
		alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#link":
		alamatnya_xpath.send_keys("link? lu siapa gw tolol nyuruh nyuruh gw?")
		alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#tr_web":
		try:
			req=requests.get(k[1])
			ll=1
		except:
			ll=0
		if ll==1:
			ll=0
			html=BeautifulSoup(req.text,"html.parser")
			zz=html.find("body")
			zz=zz.text
			xx = ""
			for i in zz.split():
				xx += i+" "
			print(xx)
			result = translator.translate(xx, src='en', dest='id')
			zz=result.text
			pyperclip.copy(str(zz))
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)

	elif k[0]=="#cuaca":
		try:
			os.system("curl wttr.in/"+k[1]+">6.txt")
			ll=1
		except:
			ll=0
		if ll==1:
			p=open('6.txt','r')
			p=p.read()
			klk=p.split("\n")
			klk=klk[len(klk)-1]
			k=p.split("└┴┴┴┘")

			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split("")
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x2)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x3)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x4)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x5)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			l=l.replace("[0m","")
			l=l.replace("[38;5;111m","")
			l=l.replace("[38;5;250m","")
			l=l.replace("[38;5;226m","")
			l=l.replace("[38;5;208m","")
			l=l.replace("[38;5;220m","")
			l=l.replace("[1m","")
			l=l.replace("[38;5;118m","")
			l=l.replace("[38;5;196m","")
			l=l.replace("[38;5;214m","")
			l=l.replace("[38;5;240;1m","")
			l=l.replace("[38;5;21;1m","")
			l=l.replace("[38;5;202m","")
			l=l.replace("[38;5;154m","")
			l=l.replace("[38;5;190m","")
			l=l.replace("[38;5;082m","")
			k=l.split(x6)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x1)
			ll=0
			for i in k:
				ll+=1
			l=k[0]
			for i in range(ll-1):
				l=str(l)+str(k[i+1])
			k=l.split(x7)
			tt=0
			po=str(hari_ini)+" "+str(tgl)+"/"+str(bl)+"/"+str(th)+"\n"
			for x in range(4):
				po=po+str(lis[x])+"\n"
				for y in range(5):
					x+=5
					po=po+str(k[x])+"\n"
			hari_ini=hari[infowaktu[6]+1]
			po=po+"\n\n"+str(hari_ini)+" "+str(tgl+1)+"/"+str(bl)+"/"+str(th)+"\n"
			for x in range(4):
				po=po+str(lis[x])+"\n"
				yt=29+x
				for y in range(5):
					yt+=5
					po=po+str(k[yt])+"\n"
			hari_ini=hari[infowaktu[6]+2]
			po=po+"\n\n"+str(hari_ini)+" "+str(tgl+2)+"/"+str(bl)+"/"+str(th)+"\n"
			for x in range(4):
				po=po+str(lis[x])+"\n"
				yt=58+x
				for y in range(5):
					yt+=5
					po=po+str(k[yt])+"\n"
			pyperclip.copy(str(klk)+"\n"+str(po))
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)
"""
	if "#T00LSB0T" not in o:
		ghg=0
		ll=1
		for Data in BigData1:
			D = Data.split("\n")
			aksi = D[0]
			reaksi = D[1]
			reaksi = reaksi.split(";")
			for word in aksi.split(";"):
				if word.lower() in o.lower():
					random.shuffle(reaksi)
					ghg=str(reaksi[0])
					o = ""
		for Data in BigData4:
			D = Data.split("\n")
			aksi = D[0]
			reaksi = D[1]
			reaksi = reaksi.split(";")
			for word in aksi.split(";"):
				if word.lower() == o.lower():
					random.shuffle(reaksi)
					ghg=str(reaksi[0])
					o = ""
		if "salam" in o.lower():
			ghg="waalaikumusallam"
			o=""
		# for word in BigData5.split(";"):
		# 	try:
		# 		if word in o.lower():
		# 			po=1
		# 			if nama_pengirim_pesan == "Oskhar":
		# 				random.shuffle(daftar_nama1)
		# 				ghg=str(daftar_nama1[0])
		# 				o=""
		# 				po=0
		# 			elif nama_pengirim_pesan=="":
		# 				z+=0
		# 			for word in daftar_nama2:
		# 				Word=word.split(";")
		# 				WD=Word[0]
		# 				if nama_pengirim_pesan==WD:
		# 					random.shuffle(daftar_nama3)
		# 					ghg=str(daftar_nama3[0]+Word[1])
		# 					o=""
		# 					po=0
		# 			if po == 1:
		# 				tambah_daftar_nama.write("\n"+nama_pengirim_pesan)
		# 				alamatnya_xpath.send_keys("Namamu tak terdaftar di dalam DataBase")
		# 				alamatnya_xpath.send_keys(Keys.ENTER)

		# 	except:
		# 		z+=0
		# for word in aksi_univers.split(";"):
		# 	if word.lower() in o.lower():
		# 		for Data in BigData3:
		# 			D = Data.split("\n")
		# 			aksi = D[0]
		# 			reaksi = D[1]
		# 			reaksi = reaksi.split(";")
		# 			for wd in aksi.split(";"):
		# 				if wd.lower() in o.lower():
		# 					random.shuffle(reaksi)
		# 					ghg=str(reaksi[0])
		# 					ll=0
		# 					o=""
		# 		if ll==1:
		# 			random.shuffle(reaksi_univers)
		# 			ghg=str(reaksi_univers[0])
		# 			ll=0
		# 			o =""
		if ghg==0:
			tambah_BigData = open("BigData.txt","a")
			if ttk==1:
				isi_pesan=o
				tambah_BigData.write("\n"+isi_pesan)
				ttk=0
			elif ttk==0:
				ttk=2
				if o!=isi_pesan:
					tambah_BigData.write(";"+o)
		else:
			ghg=ghg.replace("\n","")
			pyperclip.copy(str(ghg)+"\n\n*#T00LSB0T*")
			alamatnya_xpath.send_keys(Keys.CONTROL+"v")
			alamatnya_xpath.send_keys(Keys.ENTER)
			time.sleep(1)
			ttk=1
"""