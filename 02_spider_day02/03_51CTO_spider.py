import json

from requests_html import AsyncHTMLSession   # 导入异步模块

asession = AsyncHTMLSession()

BASE_URL = "http://edu.51cto.com/courselist/index-p{}.html"

async def get_html():
    for i in range(1,3):
        r =  await asession.get(BASE_URL.format(i))   # 异步等待
        get_item(r.html)

def get_item(html):
    c_list = html.find('.cList',first=True)
    if c_list:
        items = c_list.find('.cList_Item')
        for item in items:
            title = item.find("h3",first=True).text # 课程名称
            href = item.find('h3>a',first=True).attrs["href"]  # 课程的链接地址
            class_time = item.find("div.course_infos>p:eq(0)",first=True).text
            study_nums = item.find("div.course_infos>p:eq(1)", first=True).text
            stars = item.find("div.course_infos>div", first=True).text
            course_target = item.find(".main>.course_target", first=True).text
            price = item.find(".main>.course_payinfo h4", first=True).text
            dict = {
                "title":title,
                "href":href,
                "class_time":class_time,
                "study_nums":study_nums,
                "stars":stars,
                "course_target":course_target,
                "price":price
            }
            with open('1.txt','a') as f:
                f.write(json.dump(dict) + '\n')

    else:
        print("数据解析失败")

if __name__ == '__main__':
    result = asession.run(get_html)



# def get_content():
#     session = HTMLSession()
#     r = session.get(base_url)
#     print(r.html)
#     print(r.html.links)#获取所有的链接地址
#     print(r.html.absolute_links)#获取所有的地址
#     print(r.html.find('.cList',first=True))
#     c_list = r.html.find('.cList',first=True)
#     print(c_list.text)
if __name__ == '__main__':
    result = asession.run(get_html)