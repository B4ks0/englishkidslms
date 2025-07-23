from django.urls import path
from .views import course_list, generate_quiz, quiz_review
from homework.views import homework_list

urlpatterns = [
    path('', course_list, name='course_list'),  # ✅ Ini tujuan akhirnya
    path('quiz/<int:course_id>/', generate_quiz, name='quiz_generate'),
    path("quiz/<int:course_id>/review/", quiz_review, name="quiz_review"),
]
