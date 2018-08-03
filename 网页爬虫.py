from urllib import request
from bs4 import BeautifulSoup

maxpage = 311
st = ''
for i in range(maxpage):
    url = 'http://www.zut.edu.cn/index/xwdt/' + str(i+1) + '.htm'
    k = 5
    if i == maxpage:
        k = 3
        url = 'http://www.zut.edu.cn/index/xwdt.htm'
    port = 80
    ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134'}
    page = request.Request(url, headers=ua)
    data = request.urlopen(page).read().decode('utf-8')
    soup = BeautifulSoup(data, 'html.parser')
    titles = soup.find_all('a', 'c67214')

    for title in titles:
        herf = ''
        pro = ''
        pro = title.get('href')
        for j in range(len(pro)):
            if j > k:
                herf += pro[j]
        sonLink = "http://www.zut.edu.cn/" + herf + '\n'
        st += sonLink
        print(1)
with open("articles.txt", "w") as file:
    file.write(st)
