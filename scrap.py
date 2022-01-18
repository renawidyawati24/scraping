from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests


link_1 = 'https://play.google.com/store/books/details/Alvin_Yuan_Pratama_Organisasi_arsitektur_komputer?id=13DmDwAAQBAJ'
link_2 = 'https://play.google.com/store/books/details/Alvin_Yuan_Pratama_Personal_Tracking_menggunakan_t?id=X8PYDwAAQBAJ'
link_3 = 'https://play.google.com/store/books/details/Alvin_Yuan_Pratama_Aplikasi_Pengolah_Data_Paket_Wi?id=8ljXDwAAQBAJ'
link_4 = 'https://play.google.com/store/books/details/Ade_Sobari_Administrasi_Database_SQL_Server_2019?id=ZdXsDwAAQBAJ'
link_5 = 'https://play.google.com/store/books/details/Alvin_Yuan_Pratama_DETEKSI_IN_DAN_OUT_MENGGUNAKAN?id=2mDXDwAAQBAJ'
link_6 = 'https://play.google.com/store/books/details/sudarmaster_Jago_Bikin_ePub_dengan_Aplikasi_Online?id=zCHBDAAAQBAJ'


link = [link_1, link_2, link_3, link_4, link_5, link_6]
for i in link:
    req = Request(i, headers= {'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with requests.Session() as c:
        soup = BeautifulSoup(webpage, 'html5lib')
        link = soup.find_all('div', class_='JNury Ekdcne')
        print(soup.find('h1', attrs={"itemprop":"name"}).get_text())
        print(soup.find('div', attrs={"itemprop":"description"}).get_text())
        print(soup.find('div', class_='WRRASc').get_text())
        print(soup.find('span', class_='htlgb').get_text())
        
        
        
              