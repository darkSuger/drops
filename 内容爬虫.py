from urllib import request
from bs4 import BeautifulSoup

txt = open('articles.txt', 'r')
str_s = txt.read()
test = str_s.split()
for i in range(4):
    url = test[i]
    port = 80
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    page = request.Request(url, headers=ua)
    data = request.urlopen(page).read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    con = soup.find_all('p')
    st = []
    pro = ''
    for title in con:
        pro = str(title.string)
        pro = pro.replace('\xa0', '')
        if len(pro) >= 10:
            st.append(pro)
    with open(str(i+1)+".txt", "w") as file:
        head = soup.find_all('title')
        he = ''
        for t in head:
            he = str(t.string)
            he = he.replace('\xa0', '')
            try:
                file.write('标题：'+he+'\n'+'正文：'+'\n')
            except ConnectionRefusedError as E:
                pass
        for k in st:
            try:
                file.write('     '+k+'\n')
            except ConnectionRefusedError as E:
                pass
    file.close()


