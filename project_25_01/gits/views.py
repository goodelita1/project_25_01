from django.utils import timezone
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import HashInfoForm, ImplantInfoForm, SendMailForm
from .models import HashInfoModel, ImplantInfoModel
from .tasks import send_email_task


def hash_info(request):
    if request.method =="POST":
        form = HashInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model_change_user = HashInfoModel.objects.create(hash_name = data['hash_name'],
                                                            complexity_brut = data['complexity_brut'],
                                                            edition_year = data['edition_year'],
                                                            when_used = timezone.now(),
                                                            military = data['military'])
            model_change_user.save()
            return render(request, "gits/hashinfo.html")
    else:
        form = HashInfoForm()
    return render(request, "gits/hashinfo.html", {"form": form})

def implant_info(request):
    if request.method =="POST":
        form = ImplantInfoForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            model_change_user = ImplantInfoModel.objects.create(implant_name = data['implant_name'],
                                                            buy_possibility = data['buy_possibility'],
                                                            strange_type = data['strange_type'],
                                                            defense = data['defense'])
            model_change_user.save()
            return render(request, "gits/implantinfo.html")
    else:
        form = ImplantInfoForm()
    return render(request, "gits/implantinfo.html", {"form": form})

def email_handler(request):
    if request.method=='POST':
        form = SendMailForm(request.POST)
        if form.is_valid():
            message_mail = str(request.POST.get('message_mail', ''))
            to_mail = str(request.POST.get('to_mail', ''))
            time_to_remind = str(request.POST.get('reminder', ''))
            print(time_to_remind)
            send_email_task.delay(message_mail, time_to_remind , to_mail)
            return render(request, 'gits/sendmail.html')
    else:
        form=SendMailForm()
    return render(request, 'gits/sendmail.html', {'form':form})
