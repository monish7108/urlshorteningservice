from django.shortcuts import render, HttpResponseRedirect
from .forms import urlform
from .models import urltable
from django.views import View
from .utils import urlshortener

class index(View):

    def get(self,request):
        form=urlform()
        shorturl=""
        return render(request,"urlshortening/homepage.html",{"form":form,"shorturl":shorturl})

    def post(self,request):
        form=urlform(request.POST)
        orgurl=request.POST.get("orgurl", "")
        if urltable.objects.filter(orgurl=orgurl).exists():
            shorturl=urltable.objects.get(orgurl=orgurl)
            return render(request, "urlshortening/homepage.html", {"form": form,"shorturl":shorturl.myurl})
        else:
            myurl=urlshortener()
            myurl="localhost:8000/url/to/"+myurl
            urltable.objects.create(myurl=myurl,orgurl=orgurl).save()
            return render(request, "urlshortening/homepage.html", {"form": form, "shorturl": myurl})

def redirecting(request,name):
    if request.method=="GET":
        initial="localhost:8000/url/to/"+name
        print(initial)
        a=urltable.objects.get(myurl=initial)
        url=a.orgurl
        print(url)
        return HttpResponseRedirect(url)
