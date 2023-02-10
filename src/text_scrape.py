from bs4 import BeautifulSoup
import requests

r = requests.get('https://subslikescript.com/series/Mad_Men-804503/season-1/episode-1-Smoke_Gets_in_Your_Eyes')

soup = BeautifulSoup(r.content,"html.parser")

for br in soup.find_all("br"):
    br.replace_with("\n")

div_text = soup.find("div",{"class":"full-script"}).get_text()
# print(div_text)

div_text_clean = div_text.replace("\n\n\n\n", "BREAK").replace("\n\n", "BREAK").replace("\n", " ").replace("BREAK","\n").replace("\n\n", "\n")

print(div_text_clean)