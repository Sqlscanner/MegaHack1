                        ##KİNG KONG TARAFINDAN KODLANMIŞTIR-ESATBEY35
import subprocess as sp
import sys
import requests
import random
import os
from Scripts.kelimelistesi import *
sp.call('cls', shell=True)
sp.call('color a',shell=True)
print("CODER:KİNGKONG")
print("""\nLütfen Programı Kullanmaya Başlamadan Önce Parametrelere Bakın Ve\n
py -3 MegaHack.py -p\n
Şeklinde Parametreler Nasıl Kullanılıyor Ona Bakınız.
""")
print("\nParametreler:\n\n"
      "-u:  Hedef Site\n"
      "-a:  Admin Panel Tarama\n"
      "-d:  Dizin Tarama\n"
      "-x:  XSS Açıklı Site Hack\n"
      "-D:  Dork Üretme\n"
      "-s:  SQL Açığı Tarayıcı\n"
      "-X:  XSS Açığı Tarayıcı\n"
      "-b:  Wordpress Bruteforce Atağı\n"
      "-g:  Google Dork Tarayıcı"
      "-h:  Program Hakkında Yardım\n"
      "-v:  Program Bilgileri\n"
      "-p:  Parametrelerin Kullanımları\n"
      "\nÖRNEK:py -3 MegaHack.py -u http://www.hedefsite.com -parametre\n")


def yardim():
    print("-u: Hedef Siteyi Belirlemeniz İçin Gerekli Parametre.\n")
    print("-a: Hedef Sitede Admin Panellerini Tarar.\n")
    print("-d: Hedef Sitedeki Dizinleri Tarar.\n")
    print("-x: Verdiğiniz Sitelerdeki XSS Açığından Yararlanıp Siteyi Hackler.\n")
    print("-D: Dork Üretir.\n")
    print("-s: Verdiğiniz Sitelerde SQL Açığını Tarar.\n")
    print("-X: Verdiğiniz Sitelerde XSS Açığını Tarar.\n")
    print("-b: Verdiğiniz Wordpress Sitelere Bruteforce Atağı Yapar.\n")
    print("-g: Google'da Verdiğiniz Dorku Tarar Ve Sonuçları Gösterir\n")
    print("-v: Programın Bilgilerini Verir.")


def parametlerinkullanimlari():
    print("\n||||||||||||||Parametrelerin Kullanımları||||||||||||||\n")
    print('\npy -3 "MegaHack.py" -u http://www.hedefsite.com -a \n')
    print('py -3 "MegaHack.py" -u http://www.hedefsite.com -d \n')
    print('py -3 "MegaHack.py" -x\n')
    print('py -3 "MegaHack.py" -D\n')
    print('py -3 "MegaHack.py" -s\n')
    print('py -3 "MegaHack.py" -X\n')
    print('py -3 "MegaHack.py" -b\n')
    print('py -3 "MegaHack.py" -h\n')
    print('py -3 "MegaHack.py" -v\n')


def uploadacigibulucu():
    dorklar = ['/admin/upload.php', '/upload.php', '/file-upload.php', '/upload/upload.php']
    r = requests.get(site)
    if r.status_code == 200:
        print("Açık Taranmaya Başladı!")
    else:
        print("Siteye Bağlanılamıyor Lütfen URL'i Kontrol Ediniz.")
    for i in dorklar:

        yeni = r.url + i
        hedef = requests.get(yeni, timeout=5)
        if hedef.status_code == 200:
            print("Açık Bulundu!", "[+]" + hedef.url)
        else:
            print("Açık Bulunamadı!")

def ProgramBilgileri():
    print("Program Adı: MegaHack")
    print("Versiyon: 4.0")
    print("Kodlayan: King Kong")
    print("Sorularınız İçin E-posta Adresim:esat3515@gmail.com")
    print("İyi Kullanımlar ^_^")


if len(sys.argv) < 2:
    exit()

elif sys.argv[1] in "-X" :
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    print("XSS Açığı Tarama İşlemi Başlatıldı!\n")
    from Scripts.XSSscanner import*

    XSSAcikTarayici()

elif sys.argv[1] in "-s":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    print("SQL Açığı Tarama İşlemi Başlatıldı!\n")
    from Scripts.sqlscanner import*
    SQLAcikTarayici()

elif sys.argv[1] in "-D":
    from Scripts.dorkmaker import *
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    Dorkuretici()

elif sys.argv[1] in "-x" :
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    from Scripts.xsshack import*
    XSSHack()
elif sys.argv[1] in "-g":
    from Scripts.googledorkarama import*
    sp.call('cls',shell=True)
    sp.call('color a',shell=True)
    print("MegaHack.py->>>\n")
    googledorkarama()
elif sys.argv[1] in "-u" and sys.argv[3] in "-d":
    from Scripts.dizintarayıcı import *
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    dizintarayici()


elif sys.argv[1] in "-u" and sys.argv[3] in "-a":
    from Scripts.adminpanelbulucu import *
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    adminpanelbulucu()
elif sys.argv[1] in "-v":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    ProgramBilgileri()
elif sys.argv[1] in "-u" and sys.argv[3] in "-U":
    site = sys.argv[2]
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    uploadacigibulucu()
elif sys.argv[1] in "-b":
    from Scripts.wpbruteforce import*
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    bruteforce()
elif sys.argv[1] in "-h":
    sp.call('cls', shell=True)
    sp.call('color a', shell=True)
    print("MegaHack.py->>>\n")
    yardim()
elif sys.argv[1] in "-p":
    sp.call('cls', shell=True)
    sp.call('color a',shell=True)
    print("MegaHack.py->>>\n")
    parametlerinkullanimlari()
else:
    mesaj = "Girdiğiniz Parametre Yanlış Veya Hatalı."
    print(mesaj)
    exit()