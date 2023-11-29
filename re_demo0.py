import re
import requests

for page in range(1, 5):
    print(f'现在是第{page}页的内容:')
    url = f'https://www.cqcst.edu.cn/shiziduiwu/mingshifengcai/page/{page}'
    html = requests.get(url).text
    re_html = '<div class="n_body_list3">.*</div>'
    sub_list = re.findall(re_html, html, flags=re.DOTALL)
    sub_str = sub_list[0]
    # <img src="https://www.cqcst.edu.cn/wp-content/uploads/sites/16/2023/05/最新修改杜校照片-1.jpg" alt="杜元虎  教授">
    re_img_url = f'<img src="(.*?)"'
    re_teacher_name = f'<img .*? alt="(.*?)"'
    teacher_names = re.findall(re_teacher_name, sub_str)
    img_urls = re.findall(re_img_url, sub_str)
    for i in range(0, 15):
        img_url = img_urls[i]
        teacher_name = teacher_names[i]
        if img_url:
            print(img_url)
            img_filename = img_url.split('/')[-1]
            img_format = img_filename.split('.')[-1]
            name = teacher_name.replace(' ', '')
            print('名字', name)
            if name:
                print('正在写入:', name)
                with open(name+'.'+img_format, 'wb') as f:
                    f.write(requests.get(img_urls[i]).content)
            else:
                break
        else:
            break
print('已爬取完所有图片')
