import requests

page1 = 'https://www.ss.com/lv/real-estate/flats/riga/centre/filter/'
pageN = 'https://www.ss.com/lv/real-estate/flats/riga/centre/page{}.html'

# lets set most popular user agent
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'}

with requests.Session() as sess:
    page = sess.get(page1,headers=user_agent)
    with open('data/ss_01.html','wb') as file_:
        file_.write(page.content)
    print('Done #1')

# Lets get rest of the pages
for n in range(2,6):
    print(pageN.format(n))
    page = requests.get(pageN.format(n),headers=user_agent)
    out_file_name = 'data/ss_0{}.html'.format(n)
    with open(out_file_name, 'wb') as file_:
        file_.write(page.content)
    print('Done #{}'.format(n))