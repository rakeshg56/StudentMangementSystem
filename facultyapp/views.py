from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from adminapp.models import Faculty,FacultyCourseMapping,Course


def checkfacultylogin(request):
    fid = request.POST["fid"]
    pwd = request.POST["pwd"]

    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=pwd))#max 1 obj
    print(flag)

    if flag:
        print("Login success")
        request.session["fid"]=fid  # reate session sid
        return render(request,"facultyhome.html",{"fid":fid})
    else:
        msg="Login Failed"
        return render(request,"facultylogin.html",{"message":msg})

def facultyhome(request):
    fid = request.session["fid"]
    return render(request,"facultyhome.html",{"fid":fid})

def facultycourses(request):
    fid = request.session["fid"]
    mappingcourses=FacultyCourseMapping.objects.all()
    fmcourses=[] #storing in list
    for course in mappingcourses:
        if(course.faculty.facultyid==int(fid)):
            fmcourses.append(course)
    print(fmcourses)
    dir(fmcourses)
    count=len(fmcourses)


    return render(request,"facultycourses.html",{"fid":fid,"fmcourses":fmcourses,"count":count})


def facultychangepwd(request):
    fid = request.session["fid"]
    return  render(request,"facultychangepwd.html",{"fid":fid})

def facultyupdatepwd(request):
    fid=request.session["fid"]
    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]
    print(fid,opwd,npwd)
    flag=Faculty.objects.filter(Q(facultyid=fid)&Q(password=opwd))
    if flag:
        print("Old pwd is correct")
        Faculty.objects.filter(facultyid=fid).update(password=npwd)
        print("updated")
        msg="Pwd updated"
    else:
        print("Old pwd is wrong")
        msg="pwd is not update"
    return render(request,"facultychangepwd.html",{"fid":fid,"message":msg})