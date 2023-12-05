import re
import requests
from lxml import etree
import pandas as pd

rank_list = []
title_list = []
name_list = []
time_list = []
user_agents = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}


def get_info(root: etree._Element):
    # print
    re_cls = r'\n|\t| - '
    re_cls_obj = re.compile(re_cls)
    # ranks
    ranks = root.xpath('//span[@class="pc_temp_num"]')

    for rank_element in ranks:
        rank = re_cls_obj.sub('', rank_element.text)
        # 判断前三
        if not rank.isdigit():
            strong_element = rank_element.find('./strong')
            rank = strong_element.text
        rank_list.append(rank)
    # titles
    titles = root.xpath('//*[@id="rankWrap"]/div[2]/ul/li/a')
    for title_element in titles:
        title_list.append(re_cls_obj.sub('', title_element.text))
        name_list.append(re_cls_obj.sub('', title_element.find('./span').text))
    # times
    times = root.xpath('//span[@class="pc_temp_time"]/text()')
    for time_element in times:
        time_list.append(re_cls_obj.sub('', time_element))


if __name__ == '__main__':
    for page in range(1, 24):
        url = f'https://www.kugou.com/yy/rank/home/{page}-8888.html?from=rank'
        html = requests.get(url, headers=user_agents).text
        root = etree.HTML(html)
        get_info(root)
    # 字典套列表 写入到一个文件中
    data = {
        'rank': rank_list,
        'title': title_list,
        'name': name_list,
        'time': time_list
    }
    # 把data形成df
    df = pd.DataFrame(data)
    df.to_excel('kugou_1.xlsx', index=False)
