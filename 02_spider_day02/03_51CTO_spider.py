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
            #todo 把它保存为一个字典 想要用json数据进行存储到我的文档里但是字符格式失败
            dict = {
                "title":title,
                "href":href,
                "class_time":class_time,
                "study_nums":study_nums,
                "stars":stars,
                "course_target":course_target,
                "price":price
            }

            with open('1.txt','a',encoding='utf-8') as f:
                f.write(title+href+class_time+study_nums+stars+course_target+price+'\n')

    else:
        print("数据解析失败")

if __name__ == '__main__':
    result = asession.run(get_html)

