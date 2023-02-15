from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# All links from main page
url_main = "https://subslikescript.com/series/Mad_Men-804503"
page = requests.get(url_main)

pageSoup = BeautifulSoup(page.text, "html.parser")
seasons = pageSoup.find_all("div", class_="season")

links = pageSoup.find_all("a")

# Create empty script df
scripts_df = pd.DataFrame()

for l in links:
    link = l['href']

    # If it's not an episode link, skip to next one
    if (link.find("episode-") == -1):
        continue

    # If it is an episode link, get the episode info
    num_season = int(re.findall(r'\d+', link)[1])
    num_episode = int(re.findall(r'\d+', link)[2])

    print("Scraping S " + str(num_season) + " E " + str(num_episode))

    episode = requests.get("https://subslikescript.com/"+link)
    episodeSoup = BeautifulSoup(episode.text, "html.parser")

    for br in episodeSoup.find_all("br"):
        drop = br.replace_with("\n")

    script = episodeSoup.find("div", class_="full-script").text

    script_clean = script.replace("\n\n\n\n", "BREAK").replace("\n\n", "BREAK").replace("\n", " ").replace("BREAK","\n").replace("\n\n", "\n")

    # Write file
    # outname = "Scripts/script_S_" + str(num_season) + "_E_" + str(num_episode) + ".txt"
    # f = open(outname, "w")
    # f.write(script_clean)
    # f.close()

    # Add to running full script database with ep info
    script_lines = script_clean.splitlines()
    script_df = pd.DataFrame()
    script_df["Text"] = script_lines
    script_df["Season"] = num_season
    script_df["Episode"] = num_episode

    scripts_df = pd.concat([scripts_df, script_df])

# Write all lines to single tsv file
outname = "./ALL_SCRIPTS.tsv"
scripts_df.to_csv(outname, sep = "\t", index=False)

print("All lines organized and written to " + outname + "\n Exiting.")