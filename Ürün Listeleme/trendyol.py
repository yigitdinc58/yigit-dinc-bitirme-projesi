import requests
from bs4 import BeautifulSoup
import pandas as pd

liste = []

for page in range(1, 2):  
    url = f"https://www.trendyol.com/kosu-bantlari-x-c104277?pi={page}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")

    ty1 = soup.find("div", attrs={"class": "prdct-cntnr-wrppr"})
    ty2 = ty1.find_all("div", attrs={"class": "p-card-wrppr with-campaign-view add-to-bs-card"})
    # ty2 değişkenindeki bütün ürünlerin verisini çekmek için for döngüsü açıyoruz
    for bütün_ürünler in ty2:
        #ürünlerin linklerini alıp ekrana yazdırıyoruz
        ürün_linkleri = bütün_ürünler.find_all("div", attrs={"class": "p-card-chldrn-cntnr card-border"})
        linkin_sonu = bütün_ürünler.a.get("href")
        linkin_bası = "https://www.trendyol.com/"
        ürünlerin_linki = linkin_bası + linkin_sonu
        print(ürünlerin_linki)
       #yeni değişken oluşturup ürünlerin linkinin bulunduğu değişkene istek atıyoruz
        r1 = requests.get(ürünlerin_linki)
        soup1 = BeautifulSoup(r1.content, "lxml")
        #fiyat bilgisini çekip ekrana yazdırıyoruz
        fiyat = soup1.find("span", attrs={"class": "prc-dsc"}).text.strip().replace("\n", "")
        print(fiyat)
        #ürünlerin adlarını çekip ekrana yazdırıyoruz
        ürünün_adi = soup1.find("h1", attrs={"class": "pr-new-br"}).text.strip()
        print(ürünün_adi)
        #verilerimizi tablo haline getiriyoruz
        liste.append([ürünün_adi, ürünlerin_linki, fiyat])
#oluşturduğumuz liste dizisinin içindeki tabloyu data frame'e çeviriyoruz        
df = pd.DataFrame(liste)
#listesimizin sütun adlarını giriyoruz
df.columns = ["ürün_adı", "link", "fiyat",]
print(df)
#excel dosyamızı oluşturuyoruz
df.to_excel("ürünler3.xlsx")        
        
        


