from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'MS.Dhoni'}
    return render(request,'dhoni.html',context=d)