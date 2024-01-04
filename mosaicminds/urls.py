from django.urls import path
from eventmanager import views

urlpatterns = [
    
    path('index/', views.index, name='api_index'),
    path('about-us/', views.about_us, name='api_about_us'),
    path('add-meeting/', views.add_meeting, name='api_add_meeting'),
    path('meeting-finder/', views.meeting_finder, name='api_meeting_finder'),
    path('volunteer/', views.volunteer, name='api_volunteer'),
    path('edit-meeting/', views.edit_meeting, name='api_edit_meeting'),
    path('meeting-list-all/', views.MeetingListAll, name='api_meeting_list_all'),

  
    path('meetings/', views.MeetingList.as_view(), name='api_meetings'),
    path('users/', views.UserList.as_view(), name='api_users'),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
