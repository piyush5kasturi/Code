from django.shortcuts import render
from .models import database
from .form import ImageForm
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
        #filename = fs.save(student_image.name, student_image)
        #uploaded_file_url = fs.url(filename)
        print(student_image, student_name, student_class)

        student_name = request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        Databaseee = database(student_name=student_name, student_class=student_class, student_image=student_image)
        Databaseee.save()
    return render(request, 'database/index.html')

def card(request):
    return render(request,'database/card.html')
