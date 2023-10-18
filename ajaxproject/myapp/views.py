from django.shortcuts import render
from django.http import JsonResponse
from .forms import StudentForm
from .models import Student
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    form = StudentForm()
    studs = Student.objects.all()
    return render(request, "myapp/home.html",{"form" : form,"studs" : studs})


# @csrf_exempt
def saveData(request):
    if request.method == "POST":
        sid = request.POST.get("sid")
        print("18",sid)
        if not sid:
            form = StudentForm(request.POST)
            if form.is_valid():
                form.save()
                stud_data = list(Student.objects.values())
                return JsonResponse({"status" : 1,"stud_data":stud_data})
            else:
                return JsonResponse({"status":0})
        else:
            stud_obj = Student.objects.get(pk=sid)
            form = StudentForm(request.POST,instance=stud_obj)
            if form.is_valid():
                form.save()
                stud_data = list(Student.objects.values())
                return JsonResponse({"status" : 1,"stud_data":stud_data})
            else:
                return JsonResponse({"status":0})
        
def delete_data(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        stud_obj = Student.objects.get(pk=id)
        if stud_obj:
            stud_obj.delete()
            return JsonResponse({"status" : 1})
        else:
            return JsonResponse({"status" : 0})
        
def update_data(request):
    if request.method == "POST":
        id = request.POST.get("sid")
        stud_obj = Student.objects.get(pk=id)
        if stud_obj:
            stud_data = {
                "sid": stud_obj.id,
                "name" : stud_obj.name,
                "email" : stud_obj.email,
                "password" : stud_obj.password
            }
            return JsonResponse(stud_data)