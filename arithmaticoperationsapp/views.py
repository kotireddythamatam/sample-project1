from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request, 'add.html')
def arithmatic(request):
    try:
        a=request.GET['t1']
        b=request.GET['t2']
        c=int(a)
        d=int(b)
    except:
        return HttpResponse('invalid request')
    operation=request.GET['op']
    if operation=='add':
        e=c+d
        return HttpResponse('<h1>sum is:'+str(e)+'</h1>')
    elif operation=='sub':
        e=c-d
        return HttpResponse('<h1>sub is:'+str(e)+'</h1>')
    elif operation=='mul':
        e=c*d
        return HttpResponse('<h1>mul is:'+str(e)+'</h1>')
    elif operation=="div":
        try:
            e=c/d
            return HttpResponse('<h1>div is:'+str(e)+'</h1>')
        except:
            return render(request, 'add.html')
