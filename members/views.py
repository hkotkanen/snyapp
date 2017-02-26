from django.shortcuts import render
from django.http import HttpResponse

from .models import Member

# Create your views here.
def new_member_application(request):
    print(request.POST['email_addr'])

    payload = request.POST

    if Member.objects.filter(email_addr=payload['email_addr']):
        return HttpResponse("S-pode käytössä.")
    else:
        new_applicant = Member(
            name=payload['name'],
            place_of_residence=payload['place_of_residence'],
            email_addr=payload['email_addr'])

        new_applicant.save()

    return HttpResponse("Tallennettu.")
