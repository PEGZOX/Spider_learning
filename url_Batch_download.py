import urllib.request  # url request
import re  # regular expression
import os  # dirs
import time

'''
url 下载网址
pattern 正则化的匹配关键词
Directory 下载目录
'''


def BatchDownload(url, pattern, Directory):
    opener = urllib.request.build_opener()


    # 获取网页内容
    content = opener.open(url).read().decode('utf8')

    # 构造正则表达式，从content中匹配关键词pattern
    raw_hrefs = re.findall(pattern, content, 0)

    # set函数消除重复元素
    hset = set(raw_hrefs)

    # 下载链接
    for href in hset:
        filename = os.path.join(Directory, href.split('/')[-1])
        if(os.path.exists(filename)):
            print(href.split('/')[-1]+' is exist!')
        else:
            print("正在下载", filename)
            urllib.request.urlretrieve(href, filename)
            print("成功下载！")

        # 无sleep间隔，网站认定这种行为是攻击，反反爬虫
        time.sleep(1)

BatchDownload('http://www.cs.toronto.edu/~vmnih/data/mass_roads/train/sat/index.html',
             'http.+?tiff',
             'F:\常用遥感样本数据集\Road and Building Detection Datasets\Roads_Training_Set_Input_images')