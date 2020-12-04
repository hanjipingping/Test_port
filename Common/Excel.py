# _*_coding:utf-8_*_
# @time :2020/11/21 10:01 下午 
# @Author :hanjiping
# Emil :799652949@qq.com
# File :Excel.py
# @software PyCharm
import openpyxl

class Manage_Excel(object):

    def __init__(self,file_name,sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name


    def open_excel(self):
        self.wk = openpyxl.load_workbook(self.file_name)
        self.sheet = self.wk[self.sheet_name]

    def get_data(self):
        self.open_excel()
        #获取表格所有数据
        data = list(self.sheet.rows)
        # list_data = []
        # for i in data:
        #     for j in i:
        #         print(j.value,end="")
        #     print()
        #获取标题
        title = [i.value for i in data[0] ]
        #获取剩余数据，与title聚合打包生成新的列表
        surplus_data = []
        for i in data[1:]:
            a = []
            for j in i:
                a.append(j.value)
            surplus_data.append(dict(zip(title,a)))
        return surplus_data
        #获取其他数据






if __name__ == "__main__":

    print(test_01)









