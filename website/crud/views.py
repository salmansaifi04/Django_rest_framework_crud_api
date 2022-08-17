from django.shortcuts import render, redirect
from .forms import studentregistration
from .models import user


# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            reg = user(name = nm, email = em, password = pm)
            reg.save()
            # fm.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    stud = user.objects.all()
    return render(request, 'add_and_show.html', {'form' : fm, 'stu' : stud})

def update(request, id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = user.objects.get(pk=id)
        fm = studentregistration(instance=pi)

    return render(request, 'update.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        dlt = user.objects.get(pk=id)
        dlt.delete()
        return redirect('/')