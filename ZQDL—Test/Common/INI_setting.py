from configparser import ConfigParser
from Common.Handel_path import Config_path
import os


class Config(ConfigParser):
    # 初始化直接读取文件数据
    def __init__(self, file_name, encoding="utf-8"):
        super().__init__()
        self.read(file_name, encoding=encoding)


# 创建config对象，获取ini中的数据，直接调用即可
config = Config(os.path.join(Config_path, 'config.ini'))

# print(config.get('login', 'password'))
