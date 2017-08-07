from django.shortcuts import render
from django.http import HttpResponse
def tut1(request):
	return HttpResponse("Tutorial 1: Setting up Django and sending HttpResponse <a href='../tut3'>To Tutorial3</a>")
def tut3(request):
	return render(request,'tut/tut3.html')
def tut4(request):
	return render(request,'tut/tut4.html')



