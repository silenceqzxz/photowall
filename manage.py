# -*- encoding=UTF-8 -*-
#做脚本工作
from photowall import app,db
from flask_script import Manager
from photowall.models import User,Image,Comment
import random

manager = Manager(app)

#与数据库交互，初始化数据库
@manager.command
def init_database():
    #删掉所有表
    db.drop_all()
    #把models.py定义的类在db创建对应表
    db.create_all()
    #添加100个用户
    for i in range(100):
        db.session.add(User('name'+str(i+1),'pwd'+str(i+1)))
        #为每个用户加3张图片
        for j in range(10):#第2个参数user_id
            db.session.add(Image(get_image_url(),i+1))
            #每个图片加3条评论
            for k in range(3):#第二个参数image_id=i*10+j+1,表示一个用户10张图片
                # user_id=i+1
                db.session.add(Comment('This is a comment'+str(k), i*10+j+1, i+1))

    #事务提交
    db.session.commit()

#随机导入一张图片
def get_image_url():
    return 'http://images.nowcoder.com/head/' + str(random.randint(0, 1000))\
                        + 't.png'

if __name__ == '__main__':
    manager.run()