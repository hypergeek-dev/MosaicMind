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
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the MosaicMind app!")

def admin_check(user):
    return user.is_staff or user.is_superuser

@login_required
@user_passes_test(admin_check)
def admin_page(request):
    if request.method == 'GET':

        return JsonResponse({'message': 'Admin Page Content'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)



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
    name = request.GET.get('name')
    meeting_time = request.GET.get('meeting_time')
    area = request.GET.get('area')


    meetings_query = Meeting.objects.all()

    if name:
        meetings_query = meetings_query.filter(name__icontains=name)
    if meeting_time:
        meetings_query = meetings_query.filter(meeting_time=meeting_time)
    if area:
        meetings_query = meetings_query.filter(area=area)

    serializer = MeetingSerializer(meetings_query, many=True)

    return JsonResponse(serializer.data, safe=False)

def meeting_detail(request, meeting_id):
    try:
        meeting = Meeting.objects.get(meeting_id=meeting_id)
        data = {
            'name': meeting.name,
            'description': meeting.description,
            'moreInfoUrl': meeting.online_meeting_url,
      
        }
        return JsonResponse(data)
    except Meeting.DoesNotExist:
        return JsonResponse({'error': 'Meeting not found'}, status=404)

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


class RegisterView(APIView):
    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Create Token here
            return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)


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
