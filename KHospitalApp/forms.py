from django import forms
from KHospitalApp.models import Appoint,ImageModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appoint
        fields =['name','date','doctor','email','department','message','phone']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image','title','price']