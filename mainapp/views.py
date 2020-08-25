from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/homepage.html')

def contact(request):
    return render(request, 'mainapp/basic.html', {'values': ['Если остались вопросы, то задавайте их по телефону', '+79775780983']})