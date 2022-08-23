import requests
import bs4

res = requests.get(
    'https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy,4io&otracker=nmenu_sub_Electronics_0_Mi')
type(res)
res.text

soup = bs4.BeautifulSoup(res.text, 'lxml')
type(soup)
h1 = soup.select('title')
h1[0].getText()
