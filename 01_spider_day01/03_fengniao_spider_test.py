import aiohttp
import asyncio
async def fetch_img_url(num):
    url = 'http://bbs.fengniao.com/forum/forum_101_{}_lastpost.html'.format(num)  # 字符串拼接
    # 或者直接写成 url = 'http://bbs.fengniao.com/forum/forum_101_1_lastpost.html'
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6726.400 QQBrowser/10.2.2265.400',
    }
    async with aiohttp.ClientSession() as session:
        # 获取轮播图地址
        async with session.get(url,headers=headers) as response:
            try:
                html = await response.text()   # 获取到网页源码
                print(html)

            except Exception as e:
                print("基本错误")
                print(e)

# 这部分你可以直接临摹
loop = asyncio.get_event_loop()
tasks = asyncio.ensure_future(fetch_img_url(1))
results = loop.run_until_complete(tasks)


