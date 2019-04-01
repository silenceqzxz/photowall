# -*- encoding=UTF-8 -*-
from photowall import db,login_manager
from datetime import datetime
import random

#图片评论
class Comment(db.Model):
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(1024))
    #评论哪张图
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'))
    #谁发的评论
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Integer, default=0) # 0 正常 1删除
    user = db.relationship('User',backref='comment')

    def __init__(self, content, image_id, user_id):
        self.content = content
        self.image_id = image_id
        self.user_id = user_id

    def __repr__(self):
        return '<Comment %d %s>' % (self.id, self.content)

#用户上传的图片对应的表
class Image(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    url = db.Column(db.String(512))#图片地址
    #外键
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    created_date = db.Column(db.DateTime)
    comments = db.relationship('Comment',backref='image') #评论

    def __init__(self,url,user_id):
        self.url = url #随机生成
        self.user_id = user_id
        self.created_date = datetime.now() #当前时间

    def __repr__(self):
        return '<Image %d %s>'%(self.id,self.url)

#ORM:User类 映射 db的user表
class User(db.Model):
    # 指定对应表名
    # __tablename__ = 'user'
    __table_args__ = {'mysql_collate': 'utf8_general_ci'}
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(80),unique=True)
    password = db.Column(db.String(32))
    salt = db.Column(db.String(32))#用于注册时密码加密
    head_url = db.Column(db.String(256))
    #邮箱激活
    # email = db.Column(db.String(256),default='1054367507@qq.com')
    # confirmed = db.Column(db.Boolean,nullable=False,default=False)
    #backref='user'参数用于通过图片查用户时
    images = db.relationship('Image', backref='user', lazy='dynamic')
    # comments

    def __init__(self,username,password,salt=''):
        self.username = username
        self.password = password
        self.salt = salt
        self.head_url = 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000))\
                        + 't.png'

    def __repr__(self):
        return '[User %d %s]'%(self.id,self.username)

