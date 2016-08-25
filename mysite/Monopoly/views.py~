#coding:utf8
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
from django.utils.timezone import now, timedelta

import datetime
from django.http import HttpResponse
import MyForms,models

def index(req):
    return render(req, "404.html")


def Chat(req):
    return render(req, "chat.html")
def GetChatList(req):
    '''
    date = datetime.date.today()
    date=datetime.datetime.strptime(str(date),'%Y-%m-%d')
    #date = now().date() + timedelta(days=0) #今天
    a=models.chatcontent.objects .filter(time__gte=date)[0]['chattxt']
    '''
    #now = datetime.datetime.now()
    #前一天
    #start = now-datetime.timedelta(hours=23, minutes=59, seconds=59)
    try:
        lastID = int(req.GET["pid"])
        kwargs = {}
        kwargs["time__gte"] = datetime.date.today()
        kwargs["id__gt"] = lastID
        all = models.chatcontent.objects.filter(**kwargs)
        #print list(a[0].chattxt)
        ret = ""
        for qset in all:
            chattxt = qset.chattxt
            if chattxt == None or chattxt == u"":
                continue
            if qset.sharesname != None and qset.sharesname != u"":
                redname = u"<font color=red>" + qset.sharesname + u"</font>"
                chattxt = chattxt.replace(qset.sharesname,redname)
            ret += u"<li pid=" + str(qset.id) + u" class='chattxt'><span>"
            format_birth = u""
            if qset.time != None:
                format_birth = qset.time.strftime("%m-%d %H:%M:%S") 
            ret += format_birth + u"</span>"
            ret += chattxt + u"</li>"
    except Exception,e:
            return HttpResponse(str(e))
    return HttpResponse(ret)# r'<li pid=123 class="chattxt"><span>今天21:43</span>Are <font color="red"><b>we</b></font> meeting today?</li>')
def SayHello(req):
    return render(req, "hello.html")

def WriteCookies(req):
    if req.method == "POST":
        form = MyForms.WriteCookieForm(req.POST)
        if form.is_valid():
            r = form.execute()
            return HttpResponse(r)
    else:
        form = MyForms.WriteCookieForm()
        return render(req, "WriteCookie.html", {"form":form})
            
