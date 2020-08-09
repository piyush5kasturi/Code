from django.shortcuts import render
from .models import database
from .form import ImageForm
from math import ceil
from django.core.files.storage import FileSystemStorage
# from .models import Post
from django.http import HttpResponse

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        student_name = request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        student_image = request.FILES['image']
        fs = FileSystemStorage()
        print(student_image, student_name, student_class)
        student_name = request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        Databaseee = database(student_name=student_name, student_class=student_class, student_image=student_image)
        Databaseee.save()
    data=database.objects.all()
    print(data)
    n=len(data)
    nslides=n//4+ceil((n/4)-(n//4))
    params={'no_of_slides':nslides,'range': range(1,nslides) , 'database': data}
    return render(request, 'database/index.html',params)

def card(request):
    return render(request,'database/card.html')
