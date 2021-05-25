from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse #takes name of voew and gets what acutal url path should be so no need ot hard code url into django instead reference by name and change in one place will reflect everywhere





# Create your views here.
def index(request):
    return render(request, "search/welcome.html")

def results(request, entry):
if request.method == "POST":
    userEntry = entry
    #List = get form API
    return render(request, "search/results.html", {
        #"List": List //pass in the list to ouur html
    })
