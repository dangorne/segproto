from django.db import models
from django.forms import ModelForm

class Upload(models.Model):
    file = models.FileField(upload_to="")
    upload_date = models.DateTimeField(auto_now_add =True)

class UploadForm(ModelForm):
    class Meta:
        model = Upload
        fields = ('file',)
