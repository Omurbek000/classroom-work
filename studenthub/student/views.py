from django.http import HttpResponse, HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from student.models import Student
from .forms import StudentForm


def temp_func(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return HttpResponse("Bul <bold>GET</bold> method")
    elif request.method == "POST":
        return HttpResponse("Bul <bold>POST</bold> method")
    else:
        print("do nothing")


def get_students(request: HttpRequest) -> HttpResponse:
    students = Student.objects.all()
    context = {"students": students}
    return render(request, "student/main_page.html", context)


def first_form(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/get_students/")
    else:
        form = StudentForm()
    context = {"forms": form}
    return render(request, "student/base.html", context)


def edit_student(request: HttpRequest, id: int) -> HttpResponse:
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    print(student)
    if form.is_valid():
        form.save()
        return redirect("get_students")
    context = {"forms": form}
    return render(request, "student/base.html", context)
