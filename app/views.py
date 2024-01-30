from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.forms import *
from app.models import *

def create_school(request):
    ESFO=schoolform()
    d={'ESFO':ESFO}
    if request.method== 'POST':
        SFDO=schoolform(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['sname']
            sp=SFDO.cleaned_data['sprincipal']
            sl=SFDO.cleaned_data['slocation']
            e=SFDO.cleaned_data['email']
            re=SFDO.cleaned_data['reenteremail']
            so=school.objects.get_or_create(sname=sn,sprincipal=sp,slocation=sl,email=e,reenteremail=re)[0]
            so.save()
            return HttpResponse('school is created')
        else:
            return HttpResponse('Invalid data')

    return render(request,'create_school.html',d)


