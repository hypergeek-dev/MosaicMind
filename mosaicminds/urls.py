from django.conf import settings
from django.urls import path
from eventmanager import views
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.conf.urls.static import static


urlpatterns = [
    path('index/', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('add_meeting/', views.add_meeting, name='add_meeting'),
    path('meeting_finder/', views.meeting_finder, name='meeting_finder'),
    path('volunteer/', views.volunteer, name='volunteer'),
    path('edit_meeting/', views.edit_meeting, name='edit_meeting'),
    path('meeting_list_all/', views.MeetingListAll, name='meeting_list_all'),
    path('admin_page/', views.admin_page, name='admin_page'),
    path('meeting/', views.MeetingList.as_view(), name='meeting'),
    path('users/', views.UserList.as_view(), name='users'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    re_path(r'^.*$', TemplateView.as_view(template_name='index.html')),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)