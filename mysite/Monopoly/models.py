#coding:utf8
from django.db import models

# Create your models here.

class chatcontent(models.Model):
    sharesname = models.CharField( max_length=16,null=True)
    time = models.DateTimeField( null=True)#发言时间
    id = models.AutoField(models.IntegerField,primary_key=True)
    datapid = models.IntegerField(null=True)
    chattxt = models.TextField()
    def __unicode__(self):
        return self.chattxt
class users(models.Model):
    id = models.AutoField(models.IntegerField,primary_key=True)
    username = models.CharField(u'帐号名', max_length = 30)
    passwd = models.CharField(u'密码',max_length = 200)
    level = models.IntegerField(u'等级',default=0)#帐号等级
    createtime = models.DateTimeField(auto_now_add=True)#帐号创建时间
    lasttime = models.DateTimeField(auto_now=True,null=True)#帐号最后登录时间
    lastip = models.IPAddressField(u'最后登录IP', null=True)#帐号最后登录ip
    email = models.EmailField(u'邮箱',null=True)
    def __unicode__(self):
        return self.username
class buyshares(models.Model):
    id = models.AutoField(models.IntegerField,primary_key=True)
    buytime = models.DateTimeField(u'购买时间',null=True)
    selltime = models.DateTimeField(u'卖出时间',null=True)
    sharesname = models.CharField(u'股票名',max_length = 20)
    sharescode = models.CharField(u'股票代码',max_length = 10)
    reason = models.TextField(u'购买理由',null=True)
    buyprice = models.DecimalField(u'购买价格',null=True,max_digits=4, decimal_places=3)
    cellprice = models.DecimalField(u'卖出价格',null=True,max_digits=4, decimal_places=3)
    numofshares = models.IntegerField(u'股数',null=True)#数量
    def __unicode__(self):
        return self.sharesname