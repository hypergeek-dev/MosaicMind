from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Meeting, User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MeetingSerializer, UserSerializer
from django.http import JsonResponse



def index(request):

    data = {'message': '204 No Content '}
    return JsonResponse(data)


def about_us(request):
    data = {'message': '204 No Content'}
    return JsonResponse(data)


def add_meeting(request):
    data = {'message': '204 No Content'}
    return JsonResponse(data)


def meeting_finder(request):
    # Get query parameters
    name = request.GET.get('name')
    meeting_time = request.GET.get('meeting_time')
    area = request.GET.get('area')

    # Filter based on the provided parameters
    meetings_query = Meeting.objects.all()

    if name:
        meetings_query = meetings_query.filter(name__icontains=name)
    if meeting_time:
        # Adjust the format of meeting_time if necessary to match your model
        meetings_query = meetings_query.filter(meeting_time=meeting_time)
    if area:
        meetings_query = meetings_query.filter(area=area)

    # Serialize the meetings
    serializer = MeetingSerializer(meetings_query, many=True)

    # Return the serialized data
    return JsonResponse(serializer.data, safe=False)



def volunteer(request):
    data = {'message': '204 No Content'}
    return JsonResponse(data)


def edit_meeting(request):
    meeting_id = request.GET.get('meeting_id')
    try:
        meeting = Meeting.objects.get(id=meeting_id)
        serializer = MeetingSerializer(meeting)
        return JsonResponse(serializer.data)
    except Meeting.DoesNotExist:
        return JsonResponse({'error': 'Meeting not found'}, status=404)


def MeetingListAll(request):
    if request.method == 'GET':
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return JsonResponse(serializer.data, safe=False)
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


class MeetingList(APIView):
    def get(self, request, format=None):
        meetings = Meeting.objects.all()
        serializer = MeetingSerializer(meetings, many=True)
        return Response(serializer.data)

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
