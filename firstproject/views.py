from django.http import HttpResponse

def About(request):
    return HttpResponse("This is about page")

def shopping(request):
    return HttpResponse("I am mad at shopping")