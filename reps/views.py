from django.shortcuts import render
from django.http import HttpResponse
from .models import Link

# Create your views here.
def rep_list(request,*args,**kwargs):
	queryset=Link.objects.all()
	context={'object_list':queryset}
	return render(request,'home.html',context)
def rep_detail(request, pk):
    repository = Link.objects.get(pk=pk)
    context = {
        'repository': repository
    }
    return render(request, 'rep_detail.html', context)
def experience_view (request):
	
	return render (request,"experience.html", {})