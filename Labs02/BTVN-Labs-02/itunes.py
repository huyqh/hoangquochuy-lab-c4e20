from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode("utf-8")

soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid")

li_list = section.find_all("li")
data = []
for li in li_list:
    post = {}
    post["name_song"] = li.h3.string
    post["artist"] = li.h4.string
    data.append(post)


    options = {"default_search": "ytsearch", "max_downloads": 1}
    dl = YoutubeDL(options)
    dl.download([str(li.h3.string)])


pyexcel.save_as(records=data, dest_file_name="itunes.xlsx")










