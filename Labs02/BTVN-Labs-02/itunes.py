from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
url = "https://www.apple.com/itunes/charts/songs/"
html_content = urlopen("https://www.apple.com/itunes/charts/songs/").read().decode("utf-8")

soup = BeautifulSoup(html_content,"html.parser")
section = soup.find("section","section chart-grid")

li_list = section.find_all("li")
data = []
for li in li_list:
    post = {}
    a = li.h4.a
    post["title"] = a.string
    post["url"] = url + a["href"]
    data.append(post)

pyexcel.save_as(records=data, dest_file_name="dantri-excel.xlsx")





