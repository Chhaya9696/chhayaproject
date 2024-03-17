from django.shortcuts import render
from .forms import EmployeeForm

def home(request):
    return render(request,'flipkartnew.html')
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect("home")
            except:
                print("something wrong")
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})