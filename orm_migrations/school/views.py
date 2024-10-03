from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher


def students_list(request):
    template = 'school/students_list.html'
    object_list = Student.objects.all()
<<<<<<< HEAD
    teachers_list = Teacher.objects.all()
    context = {'object_list': object_list}
    # for i in object_list:
    #     print(i.teachers.get())
=======
    context = {'object_list': object_list}

>>>>>>> ec3b3c7556d62297291a04404e9dc6951832d0d7
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
