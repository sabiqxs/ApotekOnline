from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import DataObat


def index(request):
    return render(request, 'megapotek/home.html')

def registerLogin(request):
    return render(request, 'megapotek/register_login.html')

def dataobat_create(request):
    return HttpResponse("<h1>Create</h1>")

def dataobat_detail(request, id=None):
    instance = get_object_or_404(DataObat, id=id)
    context = {
        "title" : instance.title,
        "instance": instance,
    }
    return render(request, "dataobat/dataobat_detail.html", context)
def dataobat_list(request):
    queryset = DataObat.objects.all()
    context = {
        "object_list" : queryset,
        "title" : "List"
    }
    return render(request, "dataobat/dataobat.html", context)

def dataobat_update(request):
    return HttpResponse("<h1>Update</h1>")

def dataobat_delete(request):
    return HttpResponse("<h1>Delete</h1>")
