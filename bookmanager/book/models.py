from django.db import models

# Create your models here.

'''
ORM:     类      对象       属性
DB:     数据表   数据行      字段


1. 我们的模型类 需要继承自 models.Model
2. 系统会自动给我们添加一个主键--id
3. 字段
    字段名 = model.类型(选项)
    
    字段名其实就是数据表的字段名
    字段名不用使用 Python, Mysql等关键字
'''

class BookInfo(models.Model):
    # id
    name = models.CharField(max_length= 10)
    
    # 重写 str方法让admin表显示书籍名字
    def __str__(self):
        return self.name
    
class PeopleInfo(models.Model):
    name = models.CharField(max_length= 10)
    gender = models.BooleanField()
    book = models.ForeignKey('BookInfo', on_delete= models.CASCADE)