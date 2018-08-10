from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
#1. download web page
url = "http://dantri.com.vn"
# # 1.1. create connection
# conn = urlopen(url)
# # 1.2. read
# data = conn.read()
# # 1.3. decode
# html_content = data.decode("utf-8")

# print(html_content)
html_content = urlopen("http://dantri.com.vn/").read().decode("utf-8")
# print(html_content)
# save html to file
f = open("dantri.html","wb")
f.write( urlopen("http://dantri.com.vn/").read())
f.close
#2. extract ROI(region of interest)
# html,xml,xhtml
soup = BeautifulSoup(html_content,"html.parser")
# print(soup.prettify())

# find by class
ul = soup.find("ul","ul1 ulnew")
print(ul)
                       


#3. extract data
li_list = ul.find_all("li")
data = []
for li in li_list:
    post = {}
    post["name_song"] = li.h3.string
    post["artist_song"] = li.h4.string
    data.append(post)

pyexcel.save_as(records=data, dest_file_name="itunes-excel.xlsx")