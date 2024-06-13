from django.contrib import admin
from django.urls import path, include

from .import views,user_login

from django.conf import settings
from django.conf.urls.static import static

from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('index',views.INDEX,name='index'),

    path('chatbot',views.CHATBOT,name='chatbot'),

    path('404',views.PAGE_NOT_FOUND,name='404'),

    path('',views.HOME,name='home'),

    path('courses',views.COURSES,name='courses'),

    path('courses/filter-data',views.filter_data,name="filter-data"),
    
    path('search',views.SEARCH_COURSE,name="search_course"),
    
    path('course/<slug:slug>',views.COURSE_DETAILS,name="course_details"),

    path('contact',views.CONTACT,name='contact_us'),

    path('about',views.ABOUT,name='about_us'),

    path('checkout/<slug:slug>',views.CHECKOUT,name='checkout'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/signup',user_login.SIGNUP,name='signup'),

    path('dologin',user_login.DO_LOGIN,name='dologin'),

    path('accounts/logout', user_login.DO_LOGOUT, name='logout'),

    path('accounts/profile', user_login.PROFILE, name='profile'),

    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),

    path('mycourse', views.MY_COURSE, name='my_course'),

    path('course/watch-course/<slug:slug>',views.WATCH_COURSE,name='watch_course'),

    path('subscribe/', app_views.subscribe, name='subscribe'),

    path('thankyou/', app_views.contact_us, name='thankyou'),


] + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)
