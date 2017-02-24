import random, string
from .models import urltable

# def urlshortener():
#     str=string.ascii_lowercase+string.ascii_uppercase
#     myurl="localhost:8000/url/to/"
#     ranurl=""
#     for i in range(6):
#         ranurl+=random.choice(str)
#     if urltable.objects.filter(myurl=myurl+ranurl).exists():
#         urlshortener()
#     else:
#         return ranurl

def urlshortener(i=1):
    str=string.ascii_lowercase+string.ascii_uppercase
    myurl="localhost:8000/url/to/"
    ranurl=""
    n=6
    if i==5:
        n+=1
    for i in range(n):
        ranurl+=random.choice(str)
    if urltable.objects.filter(myurl=myurl+ranurl).exists():
        i+=1
        urlshortener(i)
    else:
        return ranurl