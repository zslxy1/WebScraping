import requests
from bs4 import BeautifulSoup
headers = {                 #访问设置，模拟用户访问
        'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"
}
for start_num in range(0,250,25):                    #访问250个电影的页面
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)      #访问是否成功，并且返回的网址页面
    html = response.text            #输出text格式
    if response.ok:  #如果成功访问的话
        print(f"{response}访问成功!!!")
        soup = BeautifulSoup(html, 'html.parser')       #text识别
        all_titiles = soup.findAll("span",attrs={"class":"title"})      #查找span下 class为title的字段
        for titile in all_titiles:                  #寻找title
            titils_string = titile.string           #打印字符串字段，其他的不要
            if "/" not in titils_string:            #不需要/后面的字符串
                print(titils_string)
    else:            #失败返回错误码，并返回失败
        print(f"{response}访问失败!!!")

print("这是一次关于爬虫的练习")


