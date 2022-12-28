from django.shortcuts import render,HttpResponse

def servicePage(request):
    return HttpResponse("Please Login!!")

def loginPage(request):
    return render(request,'login.html')

def homePage(request):
    context = {
        "title":"Home Page",
        "name":"Rohan Thakur"
            }
    return render(request,'index.html',context)

def aboutPage(request):
    context = {
        "title":"About Page",
        "name":"Rohan Thakur"
            }
    return render(request,'aboutus.html',context)

def contactPage(request):
    context = {
        "title":"Contact Page",
        "name":"Rohan Thakur"
            }
    return render(request,'contactus.html',context)

def todoPage(request):
    context = {
        "title":"TODO Page",
        "name":"Rohan Thakur"
            }
    return render(request,'todo.html',context)
