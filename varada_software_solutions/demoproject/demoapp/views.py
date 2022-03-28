from django.shortcuts import render,HttpResponse ,redirect
from .forms import UserDetails
from .models import UserDetails as userdb
from .models import creationId
import uuid
import datetime
from django.http import JsonResponse
# Create your views here.

def home(request):
    if request.method  == 'POST':
        form = UserDetails(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                update = userdb.objects.filter(insured_phone=form.cleaned_data['insured_phone'])
            except userdb.DoesNotExist:
                update = False
            if not update:
                user = userdb(**form.cleaned_data)
                user.save()
                tra = creationId(user_id=user,trans_id=uuid.uuid4())
                tra.save()
            else:
                del form.cleaned_data['Created_date']
                update.update(**form.cleaned_data)
            return redirect(home)
    else:
        form = UserDetails()
    return render(request,'form.html',{'form':form})

def user_list(request):
    user_list = creationId.objects.values()
    print(user_list)
    return JsonResponse({"data":list(user_list)})

def details(request,trans_id):
    print(trans_id)
    phone = creationId.objects.values('user_id').get(trans_id=trans_id)
    print(phone)
    data = userdb.objects.values().get(insured_phone=phone['user_id'])
    print(data)
    form = UserDetails(data)
    form.fields['insured_phone'].widget.attrs['readonly'] = True
    form.fields['Created_date'].widget.attrs['HiddenInput'] = False

    return render(request, 'form.html', {'form': form})
