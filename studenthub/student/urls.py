from django.urls import path
from .views import get_students, temp_func, first_form, edit_student


urlpatterns = [
    path('', temp_func),
    path('first_form/', first_form, name='first_form'),
    path('get_students/', get_students, name='get_students'),
    path('edit_student/<int:id>', edit_student, name='edit_student'),
]
