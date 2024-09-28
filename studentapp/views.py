from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from adminapp.models import Student,Course
from facultyapp.models import CourseContent


def studenthome(request):
    sid = request.session["sid"]

    student=Student.objects.get(studentid=sid)

    return render(request,"studenthome.html",{"sid":sid,"student":student})

def checkstudentlogin(request):
    sid = request.POST["sid"]
    pwd = request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))#max 1 obj
    print(flag)

    if flag:
        print("Login success")
        request.session["sid"]=sid  # reate session sid
        student = Student.objects.get(studentid=sid)
        return render(request,"studenthome.html",{"sid":sid,"student":student})
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})

def studentchangepwd(request):
    sid = request.session["sid"]
    return render(request, "studentchangepwd.html", {"sid": sid})


def studentupdatepwd(request):
    sid = request.session["sid"]
    opwd = request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(sid, opwd, npwd)
    flag = Student.objects.filter(Q(studentid=sid) & Q(password=opwd))
    if flag:
        print("Old pwd is correct")
        Student.objects.filter(studentid=sid).update(password=npwd)
        print("updated")
        msg = "Pwd updated"
    else:
        print("Old pwd is wrong")
        msg = "pwd is not update"
    return render(request, "studentchangepwd.html", {"sid": sid, "message": msg})


def studentcourses(request):
    sid = request.session["sid"]
    return render(request,"studentcourses.html", {"sid": sid})


def displaystudentcourses(request):
    sid = request.session["sid"]
    ay=request.POST["ay"]
    sem=request.POST["sem"]

    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))
    return render(request,"displaystudentcourses.html",{"courses":courses,"sid":sid})

def studentcoursecontent(request):
    sid=request.session["sid"]
    content=CourseContent.objects.all()
    return render(request,"studentcoursecontent.html",{"sid":sid,"coursecontent":content})