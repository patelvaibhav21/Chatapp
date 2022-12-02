from django.shortcuts import render, redirect
from chatapp.models import Message,ichater
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def frontend(request, yourname):
    friendname = request.GET.get('friendname')
   

    
    room_details = ichater.objects.get(username=yourname)
    return render(request, 'frontend.html', {
            'yourname': yourname,
            'friendname': friendname,
            'room_details': room_details
            })
    
    
 

def checkview(request):
    
    yourname = request.POST['yourname']
    friendname = request.POST['friendname']
    print(yourname)
    
    if ichater.objects.filter(username=yourname).exists():
        return redirect('roomof/'+yourname+'/?friendname='+friendname)
    else:
        new_room = ichater.objects.create(username=yourname)
        new_room.save()
        return redirect('roomof/'+yourname+'/?friendname='+friendname)

def send(request):
    getmessage = request.POST['message']
    
    yourname = request.POST['yourname']
    

    
    new_message = ichater.objects.get(username=yourname)
    new_message.messageaya=getmessage

    new_message.save()
    print('i visited')
    return HttpResponse('Message sent successfully')

def frdMessages(request, friendname):
    frd_details = ichater.objects.get(username=friendname)
    frdmessage=frd_details.messageaya
  
    return HttpResponse(frdmessage)

def myMessages(request, myname):
    my_details = ichater.objects.get(username=myname)
    mymessage=my_details.messageaya
    print(mymessage,'iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiimmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm')
  
    return HttpResponse(mymessage)