from django.shortcuts import render


from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'aboutus.html')

def add_meeting(request):
    return render(request, 'addmeeting.html')

def edit_meeting(request):
    return render(request, 'editmeeting.html')

def meeting_finder(request):
    return render(request, 'meetingfinder.html')

def volunteer(request):
    return render(request, 'volunteer.html')
