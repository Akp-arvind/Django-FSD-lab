from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from ap4.models import Course, Student, Meeting, ProjectReg, Project # prog 7
from django.views import generic # prog 8
import csv # 9-A
from reportlab.pdfgen import canvas # 9-B # type: ignore

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
    
#prog 7
def add_project(request):
    if request.method == "POST":
        form = ProjectReg(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Record inserted successfully.</h1>")
        else:
            return HttpResponse("<h1>Record not inserted.</h1>")
    else:
        form = ProjectReg()
        return render(request,"add_project.html",{"form":form})

# prog 8
class StudentListView(generic.ListView):
    model = Student
    template_name = "student_list.html"

class StudentDetailView(generic.DetailView):
    model = Student
    template_name = "student_detail.html"

# prog 9-A
def construct_csv_from_model(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="courses_data.csv"'
    writer = csv.writer(response)
    writer.writerow(['Course Name', 'Course Code', 'Course Credits'])
    for course in courses:
        writer.writerow([course.course_name, course.course_code, course.course_credits])
    return response

# prog 9-B
def construct_pdf_from_model(request):
    courses = Course.objects.all()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="courses_data.pdf"'
    c = canvas.Canvas(response)
    c.drawString(70, 720, "Course Name")
    c.drawString(170, 720, "Course Code")
    c.drawString(270, 720, "Course Credits")
    y = 660
    for course in courses:
        c.drawString(100, y, course.course_name)
        c.drawString(200, y, course.course_code)
        c.drawString(300, y, str(course.course_credits))
        y = y - 60
    c.showPage()
    c.save()
    return response

# prog 10
def regaj(request):
    if request.method == "POST":
        sid = request.POST.get("sname")
        cid = request.POST.get("cname")
        student = Student.objects.get(id=sid)
        course = Course.objects.get(id=cid)
        res = student.enrolment.filter(id=cid)
        if res:
            return HttpResponse("<h1>Student already enrolled.</h1>")
        student.enrolment.add(course)
        return HttpResponse("<h1>Student enrolled successfully.</h1>")
    else:
        students = Student.objects.all()
        courses = Course.objects.all()
        return render(request, "regaj.html", {"students": students, "courses": courses})
    
# prog 11
def course_search_ajax(request):
    if request.method == "POST":
        cid = request.POST.get("cname")
        s = Student.objects.all()
        student_list = list()
        for student in s:
            if student.enrolment.filter(id=cid):
                student_list.append(student)
        if len(student_list) == 0:
            return HttpResponse("<h1>No Students enrolled.</h1>")
        return render(request, "selected_student.html", {"student_list": student_list})
    else:
        courses = Course.objects.all()
        return render(request, "course_search_aj.html", {"courses": courses})