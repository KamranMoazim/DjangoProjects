# this is created by me

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def mainFunc(request):
    text = request.GET.get('text', 'default')
    removePunc = request.GET.get('removePunctuation', 'off')
    capALL = request.GET.get('makeAllCapital', 'off')
    smallALL = request.GET.get('makeAllSmall', 'off')
    if removePunc == "on":
        output = ""
        puncs = """'"!,@,$,%,^,&,*,(,),_,+,=,-{[}]|\/?><,.\#;:1234567890"""
        for i in text:
            if i in puncs:
                pass
            else:
                output = output + i
        parameters = {'action':"Remove Punctuation", 'output':output}
        return render(request, 'out.html', parameters)
    elif capALL == "on":
        output = ""
        for i in text:
            if False:
                pass
            else:
                output = output + i.upper()
        parameters = {'action':"Capitalize", 'output':output}
        return render(request, 'out.html', parameters)
    elif smallALL == "on":
        output = ""
        for i in text:
            if False:
                pass
            else:
                output = output + i.lower()
        parameters = {'action':"De-Capitalize", 'output':output}
        return render(request, 'out.html', parameters)
    else:
        return HttpResponse("<h1>Error, you haven't checked any Box.</h1>")