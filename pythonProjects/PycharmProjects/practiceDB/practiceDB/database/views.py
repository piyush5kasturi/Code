from django.shortcuts import render
from.models import database
#from .models import Post
from django.http import HttpResponse
# Create your views here.

def index(request):
    if request.method=='POST':
        student_name=request.POST.get('student_name')
        student_class = request.POST.get('student_class')
        Databaseee=database(student_name=student_name,student_class=student_class)
        Databaseee.save()
        if request.method == 'POST':
            form = database(request.POST, request.FILES)
            if form.is_valid():
                #m = ExampleModel.objects.get(pk=student_id)
                m.model_pic = form.cleaned_data['image']
                m.save()
                return HttpResponse('image upload success')

    return render(request , 'database/index.html')


