# -*- encoding=UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
#增加Jinja的break扩展
app.jinja_env.add_extension('jinja2.ext.loopcontrols')
app.config.from_pyfile('app.conf')

#session_id用于flash闪回
app.secret_key = 'photowall'
#初始化数据库
db = SQLAlchemy(app)
#初始化登录对象
login_manager = LoginManager(app)
#未登录是把401未认证换成登录注册页面
login_manager.login_view = '/regloginpage/'

from photowall import views,models
