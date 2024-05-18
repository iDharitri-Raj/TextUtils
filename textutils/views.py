# I have created this file !!
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'harry', 'place': 'Mars'}
    return render(request, 'index.html', params)


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    #  Check checkboxes value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcap', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # Check which checkbox is on
    if (removepunc == 'on'):
        analyzed = ""
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for ele in djtext:
            if ele not in punc:
                analyzed = analyzed + ele
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if (fullcaps == 'on'):
        analyzed = djtext.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed

    if (extraspaceremover == 'on'):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}

    if (removepunc != 'on' and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse('error')

    # Analyze the text
    return render(request, 'analyze.html', params)
