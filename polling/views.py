from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import CreatPoll,OpenPoll
from .forms import PollForm
from django.core.mail import send_mail as sm

# Create your views here.
def index(request):
    return render(request,'index.html')


#create poll
def create(request):
    if request.method == 'POST':
        if request.POST['polltype'] == 'preference':
            select=request.POST['polltype']

            title=request.POST['Title1']
            o1=request.POST['o1']
            o2=request.POST['o2']
            o3=request.POST['o3']
            o4=request.POST['o4']

            create=CreatPoll(Title=title,o1=o1,o2=o2,o3=o3,o4=o4)
            create.save()
                
            

            return redirect('Tpolls')

        else:
            title=request.POST['Title1']
            o1=request.POST['o1']
            o2=request.POST['o2']
            o3=request.POST['o3']
            o4=request.POST['o4']
            create=OpenPoll(title=title,o1=o1,o2=o2,o3=o3,o4=o4)
            create.save()
            return redirect('Tpolls')

    else:
        form = PollForm()
        

    form=PollForm()
    context={
        'form':form
    }
    return render(request,'createpoll.html',context)


#polls display
def Tpolls(request):
    op=OpenPoll.objects.all()
    o=CreatPoll.objects.all()
    
    
    context={
        'poll':o,
        'poll1':op
    }
    return render(request,'Tpolls.html',context)


#PVS poll
def CreatePoll(request,poll_id):
    poll=CreatPoll.objects.get(pk=poll_id)
    if request.method == 'POST':

        if request.POST['on1'] == 0:
            return HttpResponseRedirect('/Createpoll/%d/'%poll.id)
        else:
            poll=CreatPoll.objects.get(pk=poll_id)
            on1=int(request.POST['on1'])
            on2=int(request.POST['on2'])
            on3=int(request.POST['on3'])
            on4=int(request.POST['on4'])

            if on1==1:
                poll.one_1+=1
            if on2==1:
                poll.two_1+=1
            if on3==1:
                poll.three_1+=1
            if on4==1:
                poll.four_1+=1

            poll.votes=poll.one_1+poll.two_1+poll.three_1+poll.four_1
            poll.on1+=int(request.POST['on1'])
            poll.on2+=int(request.POST['on2'])
            poll.on3+=int(request.POST['on3'])
            poll.on4+=int(request.POST['on4'])
            poll.save()

            return HttpResponseRedirect('/pollResult/%d/'%poll.id)
    
    context={
        'poll':poll
    }
    return render(request,'poll.html',context)



#polls results
def pollResult(request,poll_id):
    poll=CreatPoll.objects.get(pk=poll_id)
    
    arr=[poll.on1,poll.on2,poll.on3,poll.on4]

    Ar=[poll.one_1,poll.two_1,poll.three_1,poll.four_1]

    a=[poll.o1,poll.o2,poll.o3,poll.o4]
    
    x=arr.index(min(arr))

    win=a[x]
    m=0
    for i in arr:
        if arr[x]==i:
            if Ar[x]>Ar[m]:
                win=a[x]
            else:
                win=a[m]

        m=m+1
        context={
        'poll':poll,
        'win':win 
    }


    return render(request,'pollresult.html',context)

#team
def Teams(request):
    return render(request,'team.html')


#open poll
def OpePoll(request,poll_id):
    poll=OpenPoll.objects.get(pk=poll_id)
    if request.method == 'POST':
        win=request.POST['p']
        if win == poll.o1:
            poll.on1+=1
        if win == poll.o2:
            poll.on2+=1
        if win == poll.o3:
            poll.on3+=1
        if win == poll.o4:
            poll.on4+=1

        poll.votes=poll.on1+poll.on2+poll.on3+poll.on4
        poll.save()
    
        return HttpResponseRedirect('/openResult/%d/'%poll.id)
    context={
        'poll':poll
    }
    return render(request,'openpoll.html',context)
    

def OpenResult(request,poll_id):
    poll=OpenPoll.objects.get(pk=poll_id)
    ar=[poll.on1,poll.on2,poll.on3,poll.on4]
    arr=[poll.o1,poll.o2,poll.o3,poll.o4]
    imax=ar.index(max(ar))
    Max=arr[imax]
    context={
        'win':Max,
        'poll':poll
    }
    return render(request,'OpenResult.html',context)

