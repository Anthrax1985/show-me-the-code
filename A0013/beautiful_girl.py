import requests
from bs4 import BeautifulSoup
import hashlib

pic_collection = []
pic_index = 0

def get_pic():
    url = 'http://tieba.baidu.com/p/2166231880'
    link_collection = []
    try:
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'lxml')
        contents = soup.findAll('div', {'class': 'p_content'})
        for content in contents:
            images = content.findAll('img')
            for img in images:
                link = img.get('src')
                if link in link_collection:
                    continue
                link_collection.append(link)
                print(link)
                download_pic(link)
    except Exception as e:
        print(e)
    finally:
        print('ok')


def download_pic(link):
    response = requests.get(link).content
    sign = hashlib.md5(response).digest()
    if sign in pic_collection:
        return
    pic_collection.append(sign)
    global pic_index
    with open('image-%d.jpg' % pic_index, 'wb') as f:
        f.write(response)
    pic_index += 1


if __name__ == '__main__':
    get_pic()