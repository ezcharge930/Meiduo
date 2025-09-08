from django.db import models

# Create your models here.

class BookInfo(models.Model):
    name = models.CharField(max_length= 10, unique= True, verbose_name= '名字')
    pub_date = models.DateField(null= True)
    readcount = models.IntegerField(default= 0)
    commentcount = models.IntegerField(default= 0)
    is_delete = models.BooleanField(default= False)
    
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理'
        
class PeopleInfo(models.Model):
    
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )
    
    name = models.CharField(max_length= 10, unique= True)
    gender = models.SmallIntegerField(choices= GENDER_CHOICE, default= 1)
    description = models.CharField(max_length= 100, null= True)
    is_delete = models.BooleanField(default= False)

    book = models.ForeignKey(BookInfo)
