
import random

import requests
from jsonpath import jsonpath

from common.handle_config import conf
from common.handle_db import db




def random_phone():
    """随机生成一个未注册手机号"""
    while True:
        phone = "131"
        for i in range(8):
            i = random.randint(0, 9)
            phone += str(i)
        # 判断改手机号是否已注册
        sql = "SELECT * FROM futureloan.member WHERE mobile_phone={}".format(phone)
        res = db.find_data(sql)
        if not res:
            return phone


def register(user_conf, pwd_conf, type=1):
    """注册,保存到配置文件"""
    url = conf.get("env", "base_url") + "/member/register"
    params = {"mobile_phone": random_phone(),
              "pwd": "12345678",
              "type": type,
              }
    headers = eval(conf.get("env", "headers"))
    requests.request(url=url, method="post", json=params, headers=headers)
    mobile = str(params["mobile_phone"])
    pwd = str(params["pwd"])
    # 保存到配置文件
    conf.write_data("test_data", user_conf, mobile)
    conf.write_data("test_data", pwd_conf, pwd)
    return mobile, pwd


def login(mobile, pwd):
    """登录"""
    login_url = conf.get("env", "base_url") + "/member/login"
    login_params = {"mobile_phone": mobile,
                    "pwd": pwd}
    headers = eval(conf.get("env", "headers"))
    response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
    res = response.json()
    # 提取token
    token = "Bearer" + " " + jsonpath(res, "$..token")[0]
    # 提取用户id
    member_id = jsonpath(res, "$..id")[0]
    return token, member_id


def recharge(token, member_id, money=500000):
    """充值"""
    headers = eval(conf.get("env", "headers"))
    headers["Authorization"] = token
    recharge_url = conf.get("env", "base_url") + "/member/recharge"
    recharge_params = {"member_id": member_id,
                       "amount": money}
    requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)


def init_env_data():
    # 注册普通用户（借款人），保存到配置文件
    user_info = register(user_conf="mobile", pwd_conf="pwd")
    # 注册普通用户（投资人），保存到配置文件
    user2 = register(user_conf="invest_mobile", pwd_conf="invest_pwd")
    # 注册管理员，保存到配置文件
    register(user_conf="admin_mobile", pwd_conf="admin_pwd", type=0)

    # (借款人)登录获取用户id
    token, member_id = login(*user_info)
    # 给用户充值
    recharge(token, member_id)
    recharge(token, member_id)

    # (投资人)登录获取用户id
    token2, member_id2 = login(*user2)
    # 给用户充值
    recharge(token2, member_id2)
    recharge(token2, member_id2)

#
# def init_env_data():
#     """初始化测试所需的环境数据"""
#     # -----------第一件事情：注册普通用户账号，保存到配置文件-----------------
#     url = conf.get("env", "base_url") + "/member/register"
#     params = {"mobile_phone": random_phone(),
#               "pwd": "12345678",
#               "type": 1,
#               }
#     headers = eval(conf.get("env", "headers"))
#     response = requests.request(url=url, method="post", json=params, headers=headers)
#
#     if response.json()["code"] == 0:
#         login_url = conf.get("env", "base_url") + "/member/login"
#         login_params = {"mobile_phone": params["mobile_phone"],
#                         "pwd": "12345678"}
#         response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
#         res = response.json()
#
#         if res["code"] == 0:
#             token = "Bearer" + " " + jsonpath(res, "$..token")[0]
#             # 提取用户id
#             member_id = jsonpath(res, "$..id")[0]
#             # 把注册的账号密码保存到配置文件
#             conf.write_data("test_data", "mobile", str(params["mobile_phone"]))
#             conf.write_data("test_data", "pwd", str(params["pwd"]))
#             # 第二件事情，给账号充值
#             headers["Authorization"] = token
#             recharge_url = conf.get("env", "base_url") + "/member/recharge"
#             recharge_params = {"member_id": member_id,
#                                "amount": 500000}
#             requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)
#             requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)
#         else:
#             raise ValueError("测试环境数据初始化失败！")
#     else:
#         raise ValueError("测试环境数据初始化失败！")
#
#     # -----------------注册管理员账户，保存到配置文件-------------------------
#     admin_params = {"mobile_phone": random_phone(),
#                     "pwd": "12345678",
#                     "type": 0, }
#     response = requests.request(url=url, method="post", json=admin_params, headers=headers)
#     if response.json()["code"] == 0:
#         conf.write_data("test_data", "admin_mobile", str(admin_params["mobile_phone"]))
#         conf.write_data("test_data", "admin_pwd", str(admin_params["pwd"]))
#
#     # -----------------注册投资账户，保存到配置文件-------------------------
#     url = conf.get("env", "base_url") + "/member/register"
#     params = {"mobile_phone": random_phone(),
#               "pwd": "12345678",
#               "type": 1,
#               }
#     headers = eval(conf.get("env", "headers"))
#     response = requests.request(url=url, method="post", json=params, headers=headers)
#
#     if response.json()["code"] == 0:
#         login_url = conf.get("env", "base_url") + "/member/login"
#         login_params = {"mobile_phone": params["mobile_phone"],
#                         "pwd": "12345678"}
#         response = requests.request(url=login_url, method="post", json=login_params, headers=headers)
#         res = response.json()
#
#         if res["code"] == 0:
#             token = "Bearer" + " " + jsonpath(res, "$..token")[0]
#             # 提取用户id
#             member_id = jsonpath(res, "$..id")[0]
#             # 把注册的账号密码保存到配置文件
#             conf.write_data("test_data", "invest_mobile", str(params["mobile_phone"]))
#             conf.write_data("test_data", "invest_pwd", str(params["pwd"]))
#             # 第二件事情，给账号充值
#             headers["Authorization"] = token
#             recharge_url = conf.get("env", "base_url") + "/member/recharge"
#             recharge_params = {"member_id": member_id,
#                                "amount": 500000}
#             requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)
#             requests.request(url=recharge_url, method="post", json=recharge_params, headers=headers)
#         else:
#             raise ValueError("测试环境数据初始化失败！")
#     else:
#         raise ValueError("测试环境数据初始化失败！")
