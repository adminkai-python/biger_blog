import os

# session设置
SECRET_KEY = os.urandom(24)


# 数据库配置
DIALECT = 'mysql'
DRIVER = 'pymysql'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'sayhello'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST
                                                 ,PORT,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False


# wtf表单设置秘钥
CSRF_ENABLED = True
SECRET_KEY = "secret hello"