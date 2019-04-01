# -*- encoding=UTF-8 -*-
from photowall import app
from photowall import db
from photowall.models import Image, User, Comment
from flask import render_template, redirect, request, flash, get_flashed_messages, send_from_directory, url_for
#flask-login核心函数和属性
from flask_login import login_user, logout_user,login_required,current_user
import random,hashlib,json,uuid,os
from photowall.qiniusdk import qiniu_upload_file

#首页
@app.route('/')
def index():
    return "让我们开始写项目吧，老铁们，加油"
