from django.shortcuts import render
from django.shortcuts import redirect
from django.db.models import Q
from .models import Employee
# Create your views here.
def home(request):
    
    if(request.method=="POST"):
        search = request.POST.get("search")
        data = Employee.objects.filter(Q(name__icontains=search) | 
        Q(city__icontains=search) | 
        Q(phone__icontains=search) | 
        Q(email__icontains=search) |
         Q(state__icontains=search) | 
         Q(salary__icontains=search))
    else:
        data = Employee.objects.all()
    return render(request,'index.html',{'data':data})
    
def delete(request, id):

    data = Employee.objects.get(id=id)
    if (data):
        data.delete()
    return redirect("/")

def addRecord(request):
    if(request.method=="POST"):
        emp= Employee()
        # table record part       =      form record part
        emp.name = request.POST.get("name")
        emp.email = request.POST.get("email")
        emp.phone = request.POST.get("phone")
        emp.salary = request.POST.get("salary")
        emp.city = request.POST.get("city")
        emp.state = request.POST.get("state")
        emp.save()
        return redirect("/")

    return render(request,'add.html')

def updateRecord(request, id ):
    data = Employee.objects.get(id=id)
    if(request.method=="POST"):
        data.name = request.POST.get("name")
        data.email = request.POST.get("email")
        data.phone = request.POST.get("phone")
        data.salary = request.POST.get("salary")
        data.city = request.POST.get("city")
        data.state = request.POST.get("state")
        data.save()
        return redirect("/")
    return render(request,'update.html',{'data':data})




      