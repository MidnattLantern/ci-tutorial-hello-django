from django.shortcuts import render, HttpResponse


def say_goaty(request):
    html_content = "<h1>Hello</h1><p>This is an HTML response.</p>"
    html_content2 = "<p>goaty cheese</p>"
    return HttpResponse(html_content + html_content2)


def say_goaty2(request):
    return render(request, 'goatapp/say_goaty2.html')