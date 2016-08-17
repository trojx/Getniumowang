#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.


from django.http import HttpResponse
import MyForms
def index(req):
    return render(req, "404.html")


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
            