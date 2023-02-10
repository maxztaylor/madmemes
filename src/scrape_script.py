from bs4 import BeautifulSoup
import requests
import re

# All links from main page
url_main = "https://subslikescript.com/series/Mad_Men-804503"
page = requests.get(url_main)

pageSoup = BeautifulSoup(page.text, "html.parser")
seasons = pageSoup.find_all("div", class_="season")

links = pageSoup.find_all("a")

for l in links:
    link = l['href']

    # If it's not an episode link, skip to next one
    if (link.find("episode-") == -1):
        continue

    # If it is an episode link, get the episode info
    num_season = int(re.findall(r'\d+', link)[1])
    num_episode = int(re.findall(r'\d+', link)[2])

    episode = requests.get("https://subslikescript.com/"+link)
    episodeSoup = BeautifulSoup(episode.text, "html.parser")

    for br in episodeSoup.find_all("br"):
        drop = br.replace_with("\n")

    script = episodeSoup.find("div", class_="full-script").text

    # Write file
    outname = "Scripts/script_S_" + str(num_season) + "_E_" + str(num_episode) + ".txt"
    f = open(outname, "w")
    f.write(script)
    f.close()















