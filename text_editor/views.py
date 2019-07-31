from django.http import HttpRequest
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def insert(request):
    text = request.POST.get('text', '')
    space_remover = request.POST.get('space_remover', 'off')
    text_cap = request.POST.get('text_cap', 'off')
    punc_remover = request.POST.get('punc_remover', 'off')
    n_line_remover = request.POST.get('n_line_remover', 'off')
    if punc_remover == "on":
        datas = text
        punc = '''!()-[]{};:'"\,<>|`./?@#$%^&*_~'''
        text = ""
        for a in datas:
            if a not in punc:
                text += a

    if n_line_remover == "on":
        datas = text
        text = ""
        for a in datas:
            if not a == "\n" and not a == "\r":
                text += a

    if space_remover == "on":
        datas = text
        text = ""
        for a in range(0,len(datas)):
            if datas[a] == " " and datas[a+1] == " ":
                pass
            else:
                text += datas[a]

    if text_cap == "on":
        datas = text
        text = ""
        for a in datas:
            text += a.upper()

    value = {"final": text}
    return render(request, "insert.html", value)

