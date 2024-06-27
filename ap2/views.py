from django.shortcuts import render
# Create your views here.
def showlist(request): 
    fruits=["Mango","Apple","Banana","Jackfruits"] 
    student_names=["Tony","Mony","Sony","Bob"]  
    return render(request,'showlist.html',{"fruits":fruits,"student_names":student_names}) 