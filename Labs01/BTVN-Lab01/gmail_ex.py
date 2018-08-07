from gmail import GMail
from gmail import Message
from random import choice
from datetime import datetime
import random as rand

gmail = GMail("huy.br31hn@gmail.com","  hsgstonghop98hp1")
html_content = """<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Cộng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; Độc lập - Tự do - Hạnh ph&uacute;c</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;<strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p>K&iacute;nh gửi: Thầy ABC</p>
<p>Họ v&agrave; t&ecirc;n: Ho&agrave;ng Quốc Huy</p>
<p>H&ocirc;m nay em viết mail n&agrave;y để xin ph&eacute;p thầy nghỉ học do {{sickness}}.</p>
<p>Em xin c&aacute;m ơn.</p>
<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;Quốc Huy.</p>
"""




list = ["em bị ốm", "chia tay ny", "ban di choi voi gai", "di choi voi ban"]

send_gmail = True

current_time = str(datetime.time(datetime.now()))
current_hour = current_time[:5]

while current_hour > "07:00" and send_gmail:
    random_choice = rand.choice(list)
    html_content = html_content.replace("{{sickness}}",random_choice)
    msg = Message( "BTVN", to = "huy.br31hn@gmail.com", html = html_content )
    gmail.send(msg)
    
    send_gmail = False

