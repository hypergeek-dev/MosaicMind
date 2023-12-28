from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Meeting, User
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MeetingSerializer, UserSerializer


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
    data = {'message': '204 No Content'}
    return JsonResponse(data)


def volunteer(request):
    data = {'message': '204 No Content'}
    return JsonResponse(data)


def edit_meeting(request):

    meeting_id = request.GET.get('meeting_id')

    try:
        meeting = Meeting.objects.get(id=meeting_id)

        data = {
            'meeting_id': meeting.meeting_id,
            'name': meeting.name,
            'area': meeting.area,
            'description': meeting.description,
            'online_meeting_url': meeting.online_meeting_url,
        }
        return JsonResponse(data) 
    except Meeting.DoesNotExist:
        data = {'error': 'Meeting not found'}
        return JsonResponse(data)


def MeetingListAll(request):
    if request.method == 'GET':
        meetings = Meeting.objects.all()

        meetings_data = [
            {
                'id': meeting.id,
                'meeting_id': meeting.meeting_id,
                'name': meeting.name,
                'meeting_time': meeting.meeting_time.strftime("%H:%M"),
                'area': meeting.area,
                'description': meeting.description,
                'online_meeting_url': meeting.online_meeting_url,
                'added_by_id': meeting.added_by_id,
               
            }
            for meeting in meetings
        ]

        return JsonResponse(meetings_data, safe=False)

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
