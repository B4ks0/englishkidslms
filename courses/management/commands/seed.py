from django.core.management.base import BaseCommand
from users.models import User
from courses.models import Course, Lesson, QuizResult
from homework.models import Homework, HomeworkTask, HomeworkSubmission
from django.utils import timezone
from datetime import date, datetime

class Command(BaseCommand):
    help = 'Seed database with initial data (users, courses, lessons, homework, tasks, submissions)'

    def handle(self, *args, **kwargs):
        # --- USERS ---
        teacher, _ = User.objects.get_or_create(
            username='Kak_Ze',
            defaults={
                'first_name': 'Josua',
                'last_name': 'Setdefit',
                'email': 'josuatambanaung@gmail.com',
                'role': 'teacher',
                'is_staff': True,
                'is_superuser': True,
                'is_active': True,
            }
        )
        teacher.set_password('password')
        teacher.save()

        student, _ = User.objects.get_or_create(
            username='Vicky',
            defaults={
                'role': 'student',
                'is_active': True,
            }
        )
        student.set_password('password')
        student.save()

        # --- COURSES ---
        course_data = [
            {
                'name': 'Simple present tense',
                'description': 'Simple Present Tense adalah bentuk waktu dalam bahasa Inggris yang digunakan untuk menyatakan... (lihat lms.sql)',
            },
            {'name': 'Simple past tense', 'description': 'Past Continuous Tense digunakan untuk menggambarkan sebuah aksi...'},
            {'name': 'Simple future tense', 'description': 'Simple Future Tense adalah cara kita berbicara tentang sesuatu yang akan terjadi...'},
            {'name': 'Present Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang sedang berlangsung saat ini.'},
            {'name': 'Present Perfect Tense', 'description': 'Digunakan untuk menyatakan aksi yang telah selesai pada waktu yang tidak spesifik di masa lalu.'},
            {'name': 'Present Perfect Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang telah dimulai di masa lalu dan masih berlangsung hingga sekarang.'},
            {'name': 'Past Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang sedang berlangsung di masa lalu.'},
            {'name': 'Past Perfect Tense', 'description': 'Digunakan untuk menyatakan aksi yang telah selesai sebelum aksi lain di masa lalu.'},
            {'name': 'Past Perfect Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang telah berlangsung sebelum aksi lain di masa lalu.'},
            {'name': 'Future Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang akan sedang berlangsung di masa depan.'},
            {'name': 'Future Perfect Tense', 'description': 'Digunakan untuk menyatakan aksi yang akan telah selesai di masa depan.'},
            {'name': 'Future Perfect Continuous Tense', 'description': 'Digunakan untuk menyatakan aksi yang akan telah berlangsung selama periode waktu tertentu di masa depan.'},
        ]
        courses = []
        for c in course_data:
            obj, _ = Course.objects.get_or_create(name=c['name'], defaults={'description': c['description'], 'teacher': teacher})
            courses.append(obj)

        # --- LESSONS ---
        Lesson.objects.get_or_create(
            course=courses[0],
            title='Daily Activities',
            defaults={
                'content': 'Simple Present Tense adalah bentuk waktu dalam bahasa Inggris yang digunakan untuk menyatakan... (lihat lms.sql)',
            }
        )

        # --- HOMEWORK ---
        hw1, _ = Homework.objects.get_or_create(
            title='Latihan Simple present tense',
            defaults={'description': 'Latihan menulis kalimat dan menyelesaikan kuis tentang simple present.'}
        )
        hw2, _ = Homework.objects.get_or_create(
            title='Latihan Simple past tense',
            defaults={'description': '-'}
        )
        hw1.assigned_to.set([teacher, student])
        hw2.assigned_to.set([teacher, student])

        # --- HOMEWORK TASKS ---
        task1, _ = HomeworkTask.objects.get_or_create(
            homework=hw1,
            task_type='quiz',
            instruction='Selesaikan kuis “Simple Present Tense” di halaman kuis.',
            quiz_keyword='Simple present tense',
            deadline=date(2025, 7, 11),
            posted_at=datetime(2025, 7, 12, 15, 6, 38)
        )
        task2, _ = HomeworkTask.objects.get_or_create(
            homework=hw1,
            task_type='catatan',
            instruction='Buat kalimat “Simple Present Tense”.',
            deadline=date(2025, 7, 11),
            posted_at=datetime(2025, 7, 12, 15, 6, 38)
        )
        task3, _ = HomeworkTask.objects.get_or_create(
            homework=hw2,
            task_type='quiz',
            instruction='Selesaikan quiz ini untuk wawasan dasar mengenai simple past tense!',
            quiz_keyword='Simple past tense',
            deadline=date(2025, 7, 18),
            posted_at=datetime(2025, 7, 13, 19, 42, 4)
        )

        # --- HOMEWORK SUBMISSIONS ---
        HomeworkSubmission.objects.get_or_create(
            student=teacher,
            task=task2,
            defaults={
                'submitted_at': datetime(2025, 7, 17, 5, 42, 19),
                'image': 'homework_uploads/Copy_of_waisak_IG_DAjdhgk.jpg',
                'quiz_completed': False,
                'is_approved': True,
            }
        )
        HomeworkSubmission.objects.get_or_create(
            student=student,
            task=task2,
            defaults={
                'submitted_at': datetime(2025, 7, 17, 5, 42, 51),
                'image': 'homework_uploads/WhatsApp_Image_2025-07-14_at_21.18.44_57ef2d81.jpg',
                'quiz_completed': False,
                'is_approved': True,
            }
        )
        HomeworkSubmission.objects.get_or_create(
            student=student,
            task=task1,
            defaults={
                'submitted_at': datetime(2025, 7, 17, 5, 47, 22),
                'quiz_completed': True,
                'is_approved': False,
            }
        )
        HomeworkSubmission.objects.get_or_create(
            student=student,
            task=task3,
            defaults={
                'submitted_at': datetime(2025, 7, 17, 5, 52, 52),
                'quiz_completed': True,
                'is_approved': False,
            }
        )

        # --- QUIZ RESULTS ---
        QuizResult.objects.get_or_create(
            user=student,
            course=courses[0],
            defaults={
                'score': 8,
                'total_questions': 10,
                'percentage': 80,
                'date_taken': datetime(2025, 7, 17, 5, 47, 22)
            }
        )
        QuizResult.objects.get_or_create(
            user=student,
            course=courses[1],
            defaults={
                'score': 7,
                'total_questions': 10,
                'percentage': 70,
                'date_taken': datetime(2025, 7, 17, 5, 52, 52)
            }
        )
        QuizResult.objects.get_or_create(
            user=student,
            course=courses[11],
            defaults={
                'score': 10,
                'total_questions': 10,
                'percentage': 100,
                'date_taken': datetime(2025, 7, 17, 10, 39, 52)
            }
        )
        QuizResult.objects.get_or_create(
            user=student,
            course=courses[2],
            defaults={
                'score': 10,
                'total_questions': 10,
                'percentage': 100,
                'date_taken': datetime(2025, 7, 17, 14, 18, 24)
            }
        )
        QuizResult.objects.get_or_create(
            user=student,
            course=courses[3],
            defaults={
                'score': 10,
                'total_questions': 10,
                'percentage': 100,
                'date_taken': datetime(2025, 7, 17, 14, 41, 58)
            }
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!')) 