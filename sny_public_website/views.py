from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # allevents = PsychoState.objects.all()
    # print([str(n) for n in allevents])
    # return HttpResponse("Hello everyone! We're at the root now.")
    return render(request, 'index.html')

def perks(request):
    raise RuntimeError("I don't know anything about that")
