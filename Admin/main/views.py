from django.shortcuts import render,redirect
from .models import *
# Create your views here.
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def Delete(request,pk):
    student = Jadval.objects.get(id=pk)
    student.delete()
    return redirect('/allsavol/')



def SavolHammasi(request):
    savol = Savollar.objects.all()
    context = {
        'savol':savol
    }
    return render(request,'savollar/savollar.html',context)


def Registration(request):
    if request.method == "POST":
        just = UserCreationForm(request.POST)
        if just.is_valid():
            just.save(request,just)
            user = just.cleaned_data.get('username')
            info = f"{user} nomli akkaunt yaratildi"
            messages.success(request,info)
            return redirect('/')
    else:
        just = UserCreationForm() 

    context={
        'just':just
    }

    return render(request,'registration/registration.html',context)



def Login(request):
    if request.method == "POST":
        username = request.POST.get['username']
        password = request.POST.get['password']
        just = authenticate(username=username,password=password)
        if just is not None:
            login(request,just)
            user = just.cleaned_data.get('usernvcame')
            info = f"{user} nomli akkaunt bilan kirildi!!"
            messages.success(request,info)
            return redirect('/')
    return render(request,'registration/login.html')


def Logout(request):
    logout(request)
    info = "Siz Akkauntdan Chiqdingiz!! "
    messages.success(info)
    return redirect('/')



def Index(request):
    return render(request,'index.html')



def AddSavol(request):
    if request.method == "POST":
        kurs = request.POST['kurs']
        fakultet = request.POST['fakultet']
        savol = request.POST['savol']
        variant1 = request.POST['variant1']
        variant2 = request.POST['variant2']
        variant3 = request.POST['variant3']
        variant4 = request.POST['variant4']
        javob = request.POST['javob']
        Savollar.objects.create(kurs = kurs,fakultet_id=fakultet,savol=savol,variant1=variant1,variant2=variant2,variant3=variant3,variant4=variant4,javob=javob)
        messages.success(request,"Savol Muvaffaqiyatli Qo'shildi!!")
        return redirect('/addsavol/')

    else:
        context={
            'savol':Savollar.objects.all(),
            'fakultet':Fakultet.objects.all()
        }
        return render(request,'savol-qoshish.html',context)

def Test(request):
    if request.method == "POST":
        savollar = Savollar.objects.all()
        togri_javob = 0
        notogri_javob = 0
        ball = 0
        umumiy = Savollar.objects.count()
        # jadval = Jadval.objects.get(togri_javob,notogri_javob,foiz,ball)
        for i in savollar:
            if i.javob == request.POST.get(i.savol):
                togri_javob+=1
                ball+=10
                # jadval.togri_javob+=1
                # jadval.ball+=10
                
            else:
                notogri_javob+=1
                # jadval.notogri_javob+=1
        foiz = (100/umumiy)*togri_javob
        context={
            'togri':togri_javob,
            'notogri':notogri_javob,
            'ball':ball,
            'foiz':foiz,
            'timer':request.POST.get('timer')
        }
        return render(request,'natija.html',context)
    else:
        context={
            'savollar':Savollar.objects.all()
        }
        return render(request,'savol.html',context)



def AddJadval(request):
    if request.method == "POST":
        kurs = request.POST['kurs']
        fakultet = request.POST['fakultet']
        ismi = request.POST['ismi']
        togri_javob = request.POST['togri_javob']
        notogri_javob = request.POST['notogri_javob']
        ball = request.POST['ball']
        foiz = request.POST['foiz']
        timer = request.POST['timer']
        sana = request.POST['sana']
        Jadval.objects.create(kurs = kurs,fakultet_id=fakultet,ismi_id=ismi,togri_javob=togri_javob,notogri_javob=notogri_javob,ball=ball,foiz=foiz,timer=timer,sana=sana)
        messages.success(request,"Jadval Muvaffaqiyatli Qo'shildi!!")
        return redirect('/addjadval/')  
    else:
        context={
            'jadval':Jadval.objects.all(),
            'user':User.objects.all(),
            'fakultet':Fakultet.objects.all()
        }
        return render(request,'bahoqoshish.html',context)


def Baholash(request):
    context={
        'jadval':Jadval.objects.all(),
        'user':User.objects.all(),
        'fakultet':Fakultet.objects.all()
    }
    return render(request,'bahoqoshish.html',context)

def Jadvallar(request):
    context={
        'jadval':Jadval.objects.all(),
        'user':User.objects.all(),
        'fakultet':Fakultet.objects.all()
    }
    return render(request,'jadval.html',context)