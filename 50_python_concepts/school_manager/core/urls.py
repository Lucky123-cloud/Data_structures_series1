from django.urls import path
from . import views
from .views import StudentListView, TeacherListView, secret_view

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', StudentListView.as_view(), name='students'),
    path('teachers/', TeacherListView.as_view(), name='teachers'),
    path('secret/', secret_view, name='secret'),
]
