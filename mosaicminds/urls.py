from django.contrib import admin
from django.urls import path
from eventmanager.views import index, about_us, add_meeting, MeetingListAll, edit_meeting, meeting_finder, volunteer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about_us, name='about_us'),
    path('add_meeting/', add_meeting, name='add_meeting'),
    path('meeting_list_all/', MeetingListAll, name='meeting_list_all'),
    path('edit_meeting/', edit_meeting, name='edit_meeting'),
    path('meeting_finder/', meeting_finder, name='meeting_finder'),
    path('volunteer/', volunteer, name='volunteer'),
]
