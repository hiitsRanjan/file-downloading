from django.shortcuts import render,redirect
from .models import FileDetails

# Create your views here.
def showIndex(request):

    return render(request,"index.html",{"data":FileDetails.objects.all()})


def save_file(request):
    file_name = request.POST.get("f1")
    file_path = request.FILES["f2"]
    FileDetails(name=file_name,file=file_path).save()
    return redirect('main')
