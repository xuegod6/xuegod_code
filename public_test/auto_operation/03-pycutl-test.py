# -*- coding: utf-8 -*-
# @Time : 2018/12/11 16:54 
# @Author : for 
# @File : 03-pycutl-test.py 
# @Software: PyCharm
from  lxml  import  etree
import  requests
import threading

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
}
base_url = 'https://www.qiushibaike.com/hot/page/%d/'
def  getPage(page):
         full_url = base_url % page
         req = requests.get(url=full_url,headers=headers)
         html = req.text
         print(html)
         html = etree.HTML(html)
         duanzi_div = html.xpath('//div[@id="content-left"]/div')
         for  duanzi  in  duanzi_div:
             wangming = duanzi.xpath('.//h2/text()')[0].strip()
             title = duanzi.xpath('.//span/text()')[0].strip()
             age = duanzi.xpath('.//div[@class="articleGender womenIcon"]/text() |.//div[@class="articleGender manIcon"]/text()')
             if  age:
                 age = age[0]
             else:
                 age = 0
             sex = duanzi.xpath('.//div[@class="articleGender womenIcon"]/@class |.//div[@class="articleGender manIcon"]/@class')
             if sex:
                 if  'man' in  sex:
                    sexer = '男'
                 elif   'women' in  sex:
                     sexer = '女'
             else:
                 sexer = '中性'
             titles = ''.join(title).strip()
             xiaolianpeople = duanzi.xpath('.//span[@class="stats-vote"]/i[@class="number"]/text()')
             xiaosun = duanzi.xpath('.//span[@class="stats-vote"][1]/text()')
             pinglun = duanzi.xpath('.//i[@class="number"]')
             #笑人数
             xp_sum =(xiaolianpeople[0]+xiaosun[0])
             #评论+人数
             pl_people=duanzi.xpath('.//span[@class="stats-comments"]/a/i[@class="number"]/text()')
             pl = duanzi.xpath('.//span[@class="stats-comments"]/a[1]/text()')[1].strip()
             #好评论人数
             xp_sum = (pl_people[0]+pl)
             #点评人
             dpr = duanzi.xpath('.//span[@class="cmt-name"]/text()')
             if  dpr:
                 dpr = dpr[0]
             else:
                 dpr = ''
             #优质评论
             yzpl = duanzi.xpath('.//div[@class="main-text"][1]/text()')
             if  yzpl:
                 yzpl = yzpl[0].strip(':')
             else:
                 yzpl = ""
             # sql = 'insert into qiushibaike(wangming,title,age,sex,xp_sum,dpr,yzpl) VALUES(%s,%s,%s,%s,%s,%s,%s) '
             # data = [wangming,title,age,sex,xp_sum,dpr,yzpl]
             # db.execute(sql,data)
             # # print(yzpl)
             # #点赞数
             # # dzp = duanzi.xpath('.//div[@class="likenum"]/text()')
             # # # if  dzp:
             # # #     dzp = dzp[0].strip()
             # # # else:
             # # #     dzp = ""
             # # print(dzp)
             # #头像
             # # duan_img = duanzi.xpath('.//div[@class="author clearfix"]//img/@src')
             # # path = os.path.join('./image/')
             # # if  not  os.path.exists(path):
             # #       os.makedirs(path)
             # # else:
             # #      print('创建成功')
             # # if  duan_img:
             # #      duanzi_img = duan_img[0]
             # #      print(duanzi_img)
             # #      duanzi_img = 'https:' + duanzi_img
             # #      fname = duanzi_img.split('/')[-1]
             # #      request.urlretrieve(duanzi_img,os.path.join(path,fname))
             # # else:
             # #      duanzi_img = ''
             # duanzi_img = duanzi.xpath('//div[@class="thumb"]//img/@src')
             # if duanzi_img:  # 段子有图片
             #       duanzi_img = duanzi_img[0]
             #       print(duanzi_img)
             #       duanzi_img = 'https:' + duanzi_img
             #       fname = duanzi_img.split('/')[-1]
             #       request.urlretrieve(duanzi_img,'./image/' + fname)
             # else:
             #       duanzi_img = ''
if __name__=='__main__':
    # db = Mysql()
    for page in range(1, 13 + 1):
        t1 = threading.Thread(target=getPage,args=(page,))
        t1.start()