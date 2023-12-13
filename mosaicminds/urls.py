
from django.contrib import admin
from django.urls import path
from eventmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),path('', views.index, name='index'),
    path('about/', views.about_us, name='about_us'),
    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('edit_meeting/', views.edit_meeting, name='edit_meeting'),
    path('meeting_finder/', views.meeting_finder, name='meeting_finder'),
    path('volunteer/', views.volunteer, name='volunteer'),
]
