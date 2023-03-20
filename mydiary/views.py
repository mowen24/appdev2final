from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from mydiary.models import Author,Entry
from django.utils import timezone

# Create your views here.

def index(request):
    return render(request, "mydiary/index.html")

def entry(request):
    entrytext = request.POST['userentry']
    try:
        a = Author.objects.get(username=request.user.username)
    except:
        a = Author(username=request.user.username).save()
    a.entry_set.create(text=entrytext, pub_date=timezone.now())
    return render(request, 'mydiary/home.html', {'entrys': Entry.objects.all()})

class HomeView(LoginRequiredMixin, View) :

    def get(self, request):
        return render(request, 'mydiary/home.html', {'entrys': Entry.objects.all()})