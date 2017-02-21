from django.conf.urls import url
from timetable import views

urlpatterns = [
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', views.LogoutView.as_view(), name='logout'),
    url(r'^home$', views.HomeView.as_view(), name='home'),
]
