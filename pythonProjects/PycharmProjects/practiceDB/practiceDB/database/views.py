from django.shortcuts import render
from.models import database
#from .models import Post
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method=='POST':
        form = database(request.POST, request.FILES)
        student_name=request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        student_image = form.cleaned_data['image']
        Databaseee=database(student_name=student_name,student_class=student_class,student_image=image)
        Databaseee.save()
    return render(request , 'database/index.html')


