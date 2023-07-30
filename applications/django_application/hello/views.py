from django.http import HttpResponse
from django.views import View


def hellow_view(request):
    return HttpResponse("Hello, I am Django application.")
