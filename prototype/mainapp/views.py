from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from mainapp.models import UploadForm, Upload
from subprocess import Popen, call
import os

def index(request):

    if request.method == "POST":
        f = UploadForm(request.POST, request.FILES)

        if f.is_valid():
            fsaved = f.save()
            command = [
                'python',
                os.getcwd() + '/mainapp/gsupload.py',
                '-k',
                format(fsaved.id),
            ]

            Popen(command)
            return HttpResponseRedirect(reverse('mainapp:index'))

    else:
        f = UploadForm()

    files = Upload.objects.all()
    return render(request, 'mainapp/index.html', {'form':f, 'files':files})
