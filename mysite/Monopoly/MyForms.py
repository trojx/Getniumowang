#coding:utf8

from django import forms

class WriteCookieForm(forms.Form):
    cookies = forms.CharField(label='cookies' ,widget=forms.Textarea)
    def execute(self):
        try:
            s = self.cleaned_data["cookies"]
            objfile = open("./houtai/cookie.txt", "w")
            objfile.write(s)
            objfile.close()
            return "ok"
        except Exception,e:
            return str(e)
