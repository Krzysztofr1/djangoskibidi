from django.shortcuts import render
from .models import klasa
# Create your views here.
def main(request):
    DANE_Z_KLASY= klasa.objects.all()
    return render(request, template_name='index.html' ,context={"ZMIENNA_HTML":DANE_Z_KLASY})