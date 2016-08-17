#coding:utf-8
from django.shortcuts import render
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.


from django.http import HttpResponse
import MyForms
def index(request):
    return HttpResponse(u"恭喜发财！")


def WriteCookies(req):
    template = loader.get_template("WriteCookie.html")
    if req.method == "POST":
        form = MyForms.WriteCookieForm(req.POST)
        if form.is_valid():
            r = form.execute()
            return HttpResponse(r)
    else:
        form = MyForms.WriteCookieForm()
        return render(req, "WriteCookie.html", {"form":form})
            