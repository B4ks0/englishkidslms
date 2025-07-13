from django.shortcuts import render, get_object_or_404
from .models import Homework, HomeworkSubmission
from django.contrib.auth.decorators import login_required
from courses.models import QuizResult, Course  # asumsi model quiz kamu bernama ini

@login_required
def homework_list(request):
    homeworks = Homework.objects.filter(assigned_to=request.user)  # type: ignore

    for hw in homeworks:
        for task in hw.tasks.all():
            task.completed = False
            task.course_id = None

            if task.task_type == 'quiz' and task.quiz_keyword:
                course = Course.objects.filter(name__icontains=task.quiz_keyword).first()  # type: ignore
                task.course_id = course.id if course else None

                done = QuizResult.objects.filter(  # type: ignore
                    user=request.user,
                    course__name__icontains=task.quiz_keyword,
                    percentage__gte=50
                ).exists()

                task.completed = done

                if done:
                    HomeworkSubmission.objects.get_or_create(  # type: ignore
                        student=request.user,
                        task=task,
                        defaults={'quiz_completed': True}
                    )

    return render(request, "homework/homework_list.html", {"homeworks": homeworks})
