from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'supriya','age':23}
    return render(request,'data_render.html',context=d)


def ifconditions(request):
    d={'a':190,'b':123,'c':9000}
    return render(request,'ifconditions.html',context=d)