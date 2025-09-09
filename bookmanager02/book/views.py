from django.shortcuts import render

from django.http import HttpRequest
from django.http import HttpResponse

from book.models import BookInfo

# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    book = BookInfo.objects.all()
    print(book)
    
    return HttpResponse('index')

############################################
from book.models import BookInfo

# 方式1
book = BookInfo(
    name = 'django',
    pub_date = '2000-1-1',
    readcount = 10,
)
# 必须调用对象的save方法才能把数据保存到数据库里面
book.save()

# 方式2
# objects -- 相当于一个代理 实现增删改查

BookInfo.objects.create(
    name = '测试开发入门',
    pub_date = '2020-1-1',
    readcount = 100,
)

#################### 修改数据 ########################
# 方式1
book = BookInfo.objects.get(id = 6)
book.name = '运维开发入门'
# 想要保存数据，需要调用对象的save方法
book.save()

# 方式2
BookInfo.objects.filter(id = 6).update(name= '爬虫入门',commentcount = 666)

#################### 删除数据 ########################
# 方式1
book = BookInfo.objects.get(id = 6)

book.delete()

# 方式2
BookInfo.objects.get(id = 6).delete()
BookInfo.objects.filter(id = 6).delete()

#################### 查询数据 ########################

# get查询的单一对象，入股不存在会抛出模型类.DoesNotExist异常
try:
    book = BookInfo.objects.get(id = 1)
except BookInfo.DoesNotExist:
    print('查询结果不存在')
book

# all查询支持多个结果
books = BookInfo.objects.all()
books

# count查询结果数量

#################### 过滤查询 ########################
# 实现SQL中的where功能，包含：
# filter过滤出多个结果
# exclude排除掉符合条件剩下的结果
# get过滤单个结果

# 模型类名.objects.filter(属性名_运算符=值)
# 模型类名.objects.exclude(属性名_运算符=值)
# 模型类名.objects.get(属性名_运算符=值)

# 查询编号为1的图书
book = BookInfo.objects.get(id = 1)
book = BookInfo.objects.get(id__exact = 1)
book = BookInfo.objects.pk(id__exact = 1)
book = BookInfo.objects.filter(id__exact = 1)

# 查询书名包含'潮'的图书