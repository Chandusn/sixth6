from django.shortcuts import render

# Create your views here.
def virat(request):
    d={'name':'Virat Kohli'}
    return render(request,'virat.html',context=d)