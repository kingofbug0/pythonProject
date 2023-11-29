import re
import requests
with open('cskjxy.data','w') as f:
    f.write()
for page in range(1, 17):

    url = f'https://www.cqcst.edu.cn/rengongzhinengyudashujuxueyuan/xueyuandongtai/page/{page}'

    res = requests.get(url)

    html = res.text

    re_sub_html = r'<div class="n_body_list1">.*?</div>'

    sub_html_list = re.findall(re_sub_html, html, flags=re.DOTALL)
    sub_html_str = sub_html_list[0]

    re_title = r'<a.*?>(.*?)</a>'
    title_list = re.findall(re_title, sub_html_str)

    re_date = r'<span>(.*?)</span>'
    date_list = re.findall(re_date, sub_html_str)

    # for title in title_list:
    #     print(title)
    #
    # for date in date_list:
    #     print(date)

    # for i in range(0, len(title_list)):
    #     print(title_list[i], date_list[i])

    datas = zip(title_list, date_list)
    for data in datas:
        print(data)
    print(url, '采集完成')
    print('===='*30)
