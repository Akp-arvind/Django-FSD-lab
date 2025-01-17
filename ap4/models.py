from django.db import models
# Create your models here.
from django.forms import ModelForm
class Course(models.Model): 
    course_code = models.CharField(max_length=40)  
    course_name = models.CharField(max_length=100)  
    course_credits = models.IntegerField(blank = True, null = True)
    # mod cred for prog 7   
    def __str__(self):
        return self.course_name # prog 6
 
class Student(models.Model):  
    student_usn = models.CharField(max_length=20)  
    student_name = models.CharField(max_length=100)  
    student_sem = models.IntegerField()  
    enrolment = models.ManyToManyField(Course)

    def __str__(self):
        return self.student_name + "(" + self.student_usn + ")" # prog 6
    
class Meeting(models.Model):
    meeting_code = models.CharField(max_length=100)  
    meeting_dt = models.DateField(auto_now_add = True)
    meeting_subject = models.CharField(max_length=100)  
    meeting_np = models.IntegerField()  

    def __str__(self):
        return self.meeting_agenda # prog 6
    
# prog 7
class Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ptopic = models.CharField(max_length=100)
    planguages = models.CharField(max_length=100)
    pduration = models.IntegerField()

class ProjectReg(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Project
        fields = ['student', 'ptopic', 'planguages', 'pduration']