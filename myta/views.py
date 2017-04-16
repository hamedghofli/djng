from django.shortcuts import render
from myta.models import mbr


def search_from(request):
#    mbr.objects.all().delete()
    return render(request,'search_form.html', {'persons':mbr.objects.all()})

    
    
    
def search_results(request):
    
    if request.method == 'GET' and 'Email' in request.GET:
        emailn = request.GET['Email']
        persons=mbr.objects.filter(email=emailn)
        if persons:
            person=persons[0]
            fname = person.first_name
            lname = person.last_name
    #        email=person.email
            return render(request, 'search_results.html',{'fname':fname,'lname':lname,'email':emailn})
        else:
            return render(request, 'search_results.html',{'email':emailn})
    else:
        
        return render(request,'search_form.html', {'persons':mbr.objects.all()})
        
        
        
        
def submit(request):
    
    if request.method == 'GET' and 'Email' in request.GET and 'Name' in request.GET and 'Last_Name' in request.GET:
        fname=request.GET['Name']
        lname=request.GET['Last_Name']
        emailn=request.GET['Email']
        persons=mbr.objects.filter(email=emailn)
        if fname and lname and emailn:
            if not persons:
                wng=mbr(first_name = fname  ,last_name = lname ,email = emailn)
                wng.save()
            else:
                wng=persons[0]
                wng.first_name = fname  
                wng.last_name = lname
                wng.emailn = emailn
                wng.save()
            return render(request,'search_form.html', {'persons':mbr.objects.all()})
        else:
            return render(request, 'search_results.html',{'fname':fname,'lname':lname,'email':emailn,'empty':True})

    else:
        return render(request,'search_form.html', {'persons':mbr.objects.all()})
