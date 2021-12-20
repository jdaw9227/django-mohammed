from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('It worked') # test django
