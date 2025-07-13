from django.shortcuts import render, get_object_or_404
from .models import Homework, HomeworkSubmission
from django.contrib.auth.decorators import login_required
from courses.models import QuizResult, Course

@login_required
def homework_list(request):
    homeworks = Homework.objects.filter(assigned_to=request.user)  # type: ignore

    for hw in homeworks:
        task_list = []  # tampung task yang sudah diproses

        for task in hw.tasks.all():
            task = task  # penting agar bisa modifikasi task sendiri
            task.completed = False
            task.course_id = None

            if task.task_type == 'quiz' and task.quiz_keyword:
                course = Course.objects.filter(name__icontains=task.quiz_keyword).first()
                task.course_id = course.id if course else None

                done = QuizResult.objects.filter(
                    user=request.user,
                    course__name__icontains=task.quiz_keyword,
                    percentage__gte=50
                ).exists()

                task.completed = done

                if done:
                    submission, created = HomeworkSubmission.objects.get_or_create(
                        student=request.user,
                        task=task,
                        defaults={'quiz_completed': True}
                    )
                    if not created and not submission.quiz_completed:
                        submission.quiz_completed = True
                        submission.save()

                # 🐛 Debug info
                print(f"[QUIZ] {task.instruction[:30]} | course_id={task.course_id} | done={done} | completed={task.completed}")

            elif task.task_type == 'upload':
                submission = HomeworkSubmission.objects.filter(
                    student=request.user,
                    task=task
                ).first()

                task.completed = submission is not None and bool(submission.image)

                print(f"[UPLOAD] {task.instruction[:30]} | uploaded={bool(submission and submission.image)}")

            else:
                task.completed = False
                print(f"[LAINNYA] {task.instruction[:30]} | completed={task.completed}")

            task_list.append(task)

        # Tambahkan hasil task yang sudah diproses ke atribut custom
        hw.enriched_tasks = task_list

    return render(request, "homework/homework_list.html", {"homeworks": homeworks})
