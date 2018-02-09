import requests

# news_tiendientu_arr=[]
# news_blogtienao_arr=[]
news_arr = []
blogtienao = "https://blogtienao.com/"
tiendientu = "https://tiendientu.com"


def get_news_tiendientu():
    global news_arr
    r = requests.get(tiendientu)
    x = r.text.split('<div class="td-module-thumb">')
    i = 1
    while (i < 2):
        content = x[i].split('class="entry-thumb"')[0]
        unpack_data = content.split('rel="bookmark"')
        link = unpack_data[0].replace('<a href=', "").replace('"', "")
        if tiendientu in link:
            if link not in news_arr:
                news_arr.append(link)
        i += 1


def get_news_blogtienao():
    global news_arr
    r = requests.get(blogtienao)
    x = r.text.split('<div class="td-module-thumb">')
    i = 1
    while (i < 2):
        content = x[i].split('class="entry-thumb"')[0]
        unpack_data = content.split('rel="bookmark"')
        link = unpack_data[0].replace('<a href=', "").replace('"', "")
        if blogtienao in link:

            if link not in news_arr:
                news_arr.append(link)
        i += 1
def news():
    get_news_tiendientu()
    get_news_blogtienao()
    return news_arr

    # news()
if __name__=='__main__':
    print(news())
