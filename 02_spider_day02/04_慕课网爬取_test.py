from urllib.parse import urljoin

import requests
#网站规律查询
# https://www.imooc.com/course/list?page=25
url_list = []

def get_page():
    base_url = 'https://www.imooc.com/course/list?page={}'
    for i in range(1,25):
        url = base_url.format(i)
        url_list.append(url)
    return url_list
def get_message(url_list):
    for i in url_list:
        pass

# if __name__ == '__main__':
#     get_page()
from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()
base_url = 'https://www.imooc.com/course/list?page={}'
async def get_html():
    for i in range(1,25):
        r = await asession.get(base_url.format(i))
        get_item(r.html)
def get_item(html):
    with open('2.txt','a',encoding='utf-8') as f:
        c_list = html.find('.course-card-container')
        if c_list:
            for item in c_list:
                title = item.find(".course-card-name",first=True).text  # 查找title
                des = item.find(".course-card-desc",first=True).text
                level = item.find(".course-card-info>span:eq(0)",first=True).text
                users = item.find(".course-card-info>span:eq(1)",first=True).text
                labels = item.find(".course-label",first=True).text.split(" ")[0]
                url = item.find("a",first=True).attrs["href"] # url拼接
                url = urljoin("https://img3.mukewang.com/",url)
                img_url = item.find("img",first=True).attrs["src"]  # url拼接
                img_url = urljoin("https://img3.mukewang.com/",img_url)
                # with open('2.txt','a') as f:
                #     f.write(title+des+level+users+labels+url+img_url+'\n')
                dict = {
                            "title":title,
                            "des":des,
                            "level":level,
                            "users":users,
                            "labels":labels,
                            "url":url,
                            "img_url":img_url
                        }
                f.write(title+des+level+users+labels+url+img_url+'\n')
    # if c_list:
    #     items = c_list.find('')
    #     for item in items:
    #         title = item.find(".course-card-name").text()  # 查找title
    #         des = item.find(".course-card-desc").text()
    #         level = item.find(".course-card-info>span:eq(0)").text()
    #         users = item.find(".course-card-info>span:eq(1)").text()
    #         labels = item.find(".course-label").text().split(" ")
    #         url = item("https://www.imooc.com/learn/", item.find("a").attr("href")) # url拼接
    #         img_url = item("https://img3.mukewang.com/", item.find("img").attr("src"))  # url拼接
    #         dict = {
    #             "title":title,
    #             "des":des,
    #             "level":level,
    #             "users":users,
    #             "labels":labels,
    #             "url":url,
    #             "img_url":img_url
    #         }
    #         print(dict)


if __name__ == '__main__':
    result = asession.run(get_html)
