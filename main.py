import requests
from bs4 import BeautifulSoup
import csv 

page_to_scrape = requests.get("https://bestsellingalbums.org/artist/13230")

soup = BeautifulSoup(page_to_scrape.text, "html.parser")

albums = soup.findAll("div", attrs={"class":"album"})

sales_of_album = soup.findAll("div", attrs={"class":"sales"})

file = open("album_sales_Stokes.CSV", "w")
writer = csv.writer(file)

writer.writerow(["ALBUMS", "SALES"])

for album, sales in zip(albums, sales_of_album):
    print(album.text + "," + sales.text)
    writer.writerow([album.text, sales.text])

file.close()
