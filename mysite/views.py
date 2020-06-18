from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    print(removepunc)
    print(djtext)
    #Analyze the text
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        parms = {'purpose': 'remove puncutation', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, "analyze.html", parms)
    if (fullcaps == 'on'):
            analyzed =''
            for char in djtext:
                analyzed = analyzed + char.upper()
            parms = {'purpose' : 'Change to  uppercasw' , 'analyzed_text': analyzed }
            djtext = analyzed
            #return render(request, 'analyze.html', parms )
    if (spaceremover == 'on'):
        analyzed = ''   
        for index, char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed = analyzed + char
        parms = {'purpose': 'remove space ', 'analyzed_text': analyzed }
        djtext = analyzed
        #return render(request, 'analyze.html', parms)
    if (newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        parms = {'purpose':' new line remover', 'analyzed_text': analyzed }
        #return render(request, 'analyze.html', parms)
        if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
            return HttpResponse("please select any operation and try again")
    return render(request, 'analyze.html', parms)
