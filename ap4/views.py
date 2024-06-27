from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from ap4.models import Course, Student

def reg(request):  
    if request.method == "POST":  
        sid=request.POST.get("sname")  
        cid=request.POST.get("cname")  
        student=Student.objects.get(id=sid)  
        course=Course.objects.get(id=cid)  
        res=student.enrolment.filter(id=cid)  
        if res:  
            return HttpResponse("<h1>Student already enrolled.</h1>")  
        student.enrolment.add(course)  
        return HttpResponse("<h1>Student enrolled successfully.</h1>")  
    else:  
        students=Student.objects.all()  
        courses=Course.objects.all() 
        return render(request,"reg.html",{"students":students, "courses":courses}) 
 
def course_search(request):  
    if request.method=="POST": 
        cid=request.POST.get("cname")  
        s=Student.objects.all()  
        student_list=list()  
        for student in s:  
            if student.enrolment.filter(id=cid):  
                student_list.append(student)  
        if len(student_list)==0:  
            return HttpResponse("<h1>No Students enrolled.</h1>") 
        return render(request,"selected_student.html",{"student_list":student_list}) 
    else:  
        courses=Course.objects.all()  
        return render(request,"course_search.html",{"courses":courses})