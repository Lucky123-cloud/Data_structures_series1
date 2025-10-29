from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Teacher
from .mixins import TimestampMixin


# Create your views here.

def home(request):
    return HttpResponse("Welcome to the School Manager Home Page!")

#------------DECORATORS------------
def staff_only(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return JsonResponse({'error': 'Unauthorized'}, status=401)
        return view_func(request, *args, **kwargs)
    return wrapper


class BaseListView(TimestampMixin):
    model = None  # To be defined in subclasses

    def get_queryset(self):
        return self.model.objects.all()
    
    def get(self, request):
        self.log_action(f"Fetching list of {self.model.__name__}s")
        queryset = self.get_queryset()
        data = [obj.introduce() for obj in queryset]
        return JsonResponse(data, safe=False)
    

#------------INHERITANCE & POLYMORPHISM------------
class StudentListView(BaseListView):
    model = Student


class TeacherListView(BaseListView):
    model = Teacher


@staff_only
def secret_view(request):
    return JsonResponse({'message': 'This is a secret view for staff only!'})