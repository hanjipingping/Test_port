import os
import time

start_time = time.time()
dirname = os.path.dirname(__file__)


def html_create():
    number = int(input('请输入要生成的网址数量：'))
    with open(os.path.join(dirname, 'html.txt'), 'w', encoding='utf-8') as file:
        for i in range(number):
            file.writelines('http:www.baidu.com' + str(i) + os.linesep)
    return


html_create()
print('生成的文件地址为：' + os.path.join(dirname, 'html.txt'))
end_time = time.time()
print(f'一共消耗的时间为：{end_time - start_time}')
