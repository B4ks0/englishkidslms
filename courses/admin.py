from django.contrib import admin
from .models import Course, Lesson
from .models import QuizResult

admin.site.register(QuizResult)
admin.site.register(Course)
admin.site.register(Lesson)
