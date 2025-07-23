from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from courses.models import Course, Lesson, QuizResult
from homework.models import Homework, HomeworkSubmission, HomeworkTask
from users.models import User
from django.utils import timezone
import datetime

class Command(BaseCommand):
    help = 'Seeds the database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Seed auth_permission
        permissions = [
            (1, 'Can add log entry', 1, 'add_logentry'),
            (2, 'Can change log entry', 1, 'change_logentry'),
            (3, 'Can delete log entry', 1, 'delete_logentry'),
            (4, 'Can view log entry', 1, 'view_logentry'),
            (5, 'Can add permission', 2, 'add_permission'),
            (6, 'Can change permission', 2, 'change_permission'),
            (7, 'Can delete permission', 2, 'delete_permission'),
            (8, 'Can view permission', 2, 'view_permission'),
            (9, 'Can add group', 3, 'add_group'),
            (10, 'Can change group', 3, 'change_group'),
            (11, 'Can delete group', 3, 'delete_group'),
            (12, 'Can view group', 3, 'view_group'),
            (13, 'Can add content type', 4, 'add_contenttype'),
            (14, 'Can change content type', 4, 'change_contenttype'),
            (15, 'Can delete content type', 4, 'delete_contenttype'),
            (16, 'Can view content type', 4, 'view_contenttype'),
            (17, 'Can add session', 5, 'add_session'),
            (18, 'Can change session', 5, 'change_session'),
            (19, 'Can delete session', 5, 'delete_session'),
            (20, 'Can view session', 5, 'view_session'),
            (21, 'Can add user', 6, 'add_user'),
            (22, 'Can change user', 6, 'change_user'),
            (23, 'Can delete user', 6, 'delete_user'),
            (24, 'Can view user', 6, 'view_user'),
            (25, 'Can add lesson', 7, 'add_lesson'),
            (26, 'Can change lesson', 7, 'change_lesson'),
            (27, 'Can delete lesson', 7, 'delete_lesson'),
            (28, 'Can view lesson', 7, 'view_lesson'),
            (29, 'Can add course', 8, 'add_course'),
            (30, 'Can change course', 8, 'change_course'),
            (31, 'Can delete course', 8, 'delete_course'),
            (32, 'Can view course', 8, 'view_course'),
            (33, 'Can add quiz result', 9, 'add_quizresult'),
            (34, 'Can change quiz result', 9, 'change_quizresult'),
            (35, 'Can delete quiz result', 9, 'delete_quizresult'),
            (36, 'Can view quiz result', 9, 'view_quizresult'),
            (37, 'Can add homework', 10, 'add_homework'),
            (38, 'Can change homework', 10, 'change_homework'),
            (39, 'Can delete homework', 10, 'delete_homework'),
            (40, 'Can view homework', 10, 'view_homework'),
            (41, 'Can add homework submission', 11, 'add_homeworksubmission'),
            (42, 'Can change homework submission', 11, 'change_homeworksubmission'),
            (43, 'Can delete homework submission', 11, 'delete_homeworksubmission'),
            (44, 'Can view homework submission', 11, 'view_homeworksubmission'),
            (45, 'Can add homework task', 12, 'add_homeworktask'),
            (46, 'Can change homework task', 12, 'change_homeworktask'),
            (47, 'Can delete homework task', 12, 'delete_homeworktask'),
            (48, 'Can view homework task', 12, 'view_homeworktask'),
            (49, 'Can add quiz', 13, 'add_quiz'),
            (50, 'Can change quiz', 13, 'change_quiz'),
            (51, 'Can delete quiz', 13, 'delete_quiz'),
            (52, 'Can view quiz', 13, 'view_quiz'),
        ]
        for perm_id, name, content_type_id, codename in permissions:
            content_type = ContentType.objects.get(id=content_type_id)
            Permission.objects.get_or_create(
                id=perm_id,
                defaults={'name': name, 'content_type': content_type, 'codename': codename}
            )

        # Seed users_user
        users = [
            (1, 'pbkdf2_sha256$1000000$A6ib0J5uLQaOs5uNQ2LJ6I$ThuO98BpFGCKfxOWzOKshlX3x8ooKsehibArmDyPS5Y=', 
             datetime.datetime(2025, 7, 17, 5, 42, 39, 68534, tzinfo=timezone.utc), True, 'Kak_Ze', 
             'Josua', 'Setdefit', 'josuatambanaung@gmail.com', True, True, 
             datetime.datetime(2025, 7, 7, 8, 52, 23, tzinfo=timezone.utc), 'teacher'),
            (2, 'pbkdf2_sha256$1000000$SZKzTaaKlwm1TUJrn6dKbw$QYjQoj63sVm2tZ4exmj2obDTAyLPZ9UXeSZj/bFjaUA=', 
             datetime.datetime(2025, 7, 17, 5, 42, 46, 711569, tzinfo=timezone.utc), False, 'Vicky', 
             '', '', '', False, True, 
             datetime.datetime(2025, 7, 7, 8, 52, 37, tzinfo=timezone.utc), 'student'),
        ]
        for user_id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role in users:
            User.objects.get_or_create(
                id=user_id,
                defaults={
                    'password': password,
                    'last_login': last_login,
                    articulo_id='is_superuser': is_superuser,
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'is_staff': is_staff,
                    'is_active': is_active,
                    'date_joined': date_joined,
                    'role': role,
                }
            )

        # Seed courses_course
        courses = [
            (1, 'Simple present tense', 'Simple Present Tense adalah bentuk waktu dalam bahasa Inggris yang digunakan untuk menyatakan:\r\n\r\nKebiasaan (habit)\r\nContoh:\r\n\r\nI go to school every day.\r\n(Saya pergi ke sekolah setiap hari.)\r\n\r\nFakta umum (general truth)\r\nContoh:\r\n\r\nThe sun rises in the east.\r\n(Matahari terbit di timur.)\r\n\r\nKeadaan sekarang yang permanen (permanent situation)\r\nContoh:\r\n\r\nShe lives in Jakarta.\r\n(Dia tinggal di Jakarta.)\r\n\r\nInstruksi atau jadwal (instructions/schedule)\r\nContoh:\r\n\r\nThe train leaves at 9 AM.\r\n(Kereta berangkat jam 9 pagi.)\r\n\r\nRumus Simple Present Tense:\r\n1. Kalamat Positif (Positive):\r\nSubject + Verb-1 (s/es jika subjek he/she/it)\r\nContoh:\r\n\r\nI eat rice.\r\n\r\nShe eats rice.\r\n\r\n2. Kalimat Negatif (Negative):\r\nSubject + do/does + not + Verb-1\r\nContoh:\r\n\r\nI do not eat rice.\r\n\r\nHe does not eat rice.\r\n\r\n3. Kalimat Tanya (Interrogative):\r\nDo/Does + subject + Verb-1?\r\nContoh:\r\n\r\nDo you eat rice?\r\n\r\nDoes she eat rice?', 1),
            (2, 'Simple past tense', 'Past Continuous Tense digunakan untuk menggambarkan sebuah aksi atau kegiatan yang sedang berlangsung di waktu tertentu di masa lampau. Bayangkan kamu sedang menyaksikan sebuah adegan dari masa lalu—seperti cuplikan film—di mana sesuatu sedang terjadi, tapi belum selesai.\r\n\r\nMisalnya, kamu bisa berkata, "I was reading a book when it started to rain." Kalimat ini memberi nuansa bahwa kegiatan membaca terjadi duluan dan sedang berlangsung ketika hujan mulai turun. Fokusnya bukan hanya pada "apa yang terjadi", tapi kapan dan bagaimana itu terjadi secara bertahap.\r\n\r\nTense ini sering dipakai dalam cerita atau kejadian yang memiliki suasana, latar, atau gangguan—seolah kamu mengajak pendengar masuk ke dalam momen yang bergerak. Contoh lainnya, "She was walking home when she saw a black cat." Kalimat ini bukan cuma menyampaikan fakta, tapi juga suasana dan waktu di mana itu terjadi.', 1),
            (3, 'Simple future tense', 'Simple Future Tense adalah cara kita berbicara tentang sesuatu yang akan terjadi. Ia digunakan saat kita membayangkan masa depan—bukan yang sedang berlangsung, bukan yang sudah lewat—tapi sesuatu yang belum terjadi, tapi akan.\r\n\r\nBayangkan kamu sedang membuat rencana atau janji. Kamu bilang, "I will study tonight." Itu artinya, kamu belum belajar sekarang, tapi kamu akan melakukannya nanti malam. Kata kuncinya di sini adalah "akan", dan dalam Bahasa Inggris bentuk ini biasanya menggunakan "will" atau kadang "be going to".\r\n\r\nKalau kamu berkata, "She will travel to Japan next year," kamu sedang membuka jendela ke masa depan, memberitahu orang lain tentang sesuatu yang akan terjadi, meskipun sekarang belum.\r\n\r\nTense ini juga dipakai untuk membuat prediksi—misalnya, "It will rain tomorrow." Kamu belum tahu pasti, tapi kamu merasa atau percaya hal itu akan terjadi.\r\n\r\nJadi, Simple Future Tense seperti janji, rencana, atau ramalan yang kamu ucapkan sekarang untuk sesuatu yang akan hidup di masa depan.', 1),
            (4, 'Present Continuous Tense', 'Digunakan untuk menyatakan aksi yang sedang berlangsung saat ini.', 1),
            (5, 'Present Perfect Tense', 'Digunakan untuk menyatakan aksi yang telah selesai pada waktu yang tidak spesifik di masa lalu.', 1),
            (6, 'Present Perfect Continuous Tense', 'Digunakan untuk menyatakan aksi yang telah dimulai di masa lalu dan masih berlangsung hingga sekarang.', 1),
            (7, 'Past Continuous Tense', 'Digunakan untuk menyatakan aksi yang sedang berlangsung di masa lalu.', 1),
            (8, 'Past Perfect Tense', 'Digunakan untuk menyatakan aksi yang telah selesai sebelum aksi lain di masa lalu.', 1),
            (9, 'Past Perfect Continuous Tense', 'Digunakan untuk menyatakan aksi yang telah berlangsung sebelum aksi lain di masa lalu.', 1),
            (10, 'Future Continuous Tense', 'Digunakan untuk menyatakan aksi yang akan sedang berlangsung di masa depan.', 1),
            (11, 'Future Perfect Tense', 'Digunakan untuk menyatakan aksi yang akan telah selesai di masa depan.', 1),
            (12, 'Future Perfect Continuous Tense', 'Digunakan untuk menyatakan aksi yang akan telah berlangsung selama periode waktu tertentu di masa depan.', 1),
        ]
        for course_id, name, description, teacher_id in courses:
            teacher = User.objects.get(id=teacher_id)
            Course.objects.get_or_create(
                id=course_id,
                defaults={'name': name, 'description': description, 'teacher': teacher}
            )

        # Seed courses_lesson
        lessons = [
            (1, 'Daily Activities', 'Simple Present Tense adalah bentuk waktu dalam bahasa Inggris yang digunakan untuk menyatakan:\r\n\r\nKebiasaan (habit)\r\nContoh:\r\n\r\nI go to school every day.\r\n(Saya pergi ke sekolah setiap hari.)\r\n\r\nFakta umum (general truth)\r\nContoh:\r\n\r\nThe sun rises in the east.\r\n(Matahari terbit di timur.)\r\n\r\nKeadaan sekarang yang permanen (permanent situation)\r\nContoh:\r\n\r\nShe lives in Jakarta.\r\n(Dia tinggal di Jakarta.)\r\n\r\nInstruksi atau jadwal (instructions/schedule)\r\nContoh:\r\n\r\nThe train leaves at 9 AM.\r\n(Kereta berangkat jam 9 pagi.)\r\n\r\nRumus Simple Present Tense:\r\n1. Kalimat Positif (Positive):\r\nSubject + Verb-1 (s/es jika subjek he/she/it)\r\nContoh:\r\n\r\nI eat rice.\r\n\r\nShe eats rice.\r\n\r\n2. Kalimat Negatif (Negative):\r\nSubject + do/does + not + Verb-1\r\nContoh:\r\n\r\nI do not eat rice.\r\n\r\nHe does not eat rice.\r\n\r\n3. Kalimat Tanya (Interrogative):\r\nDo/Does + subject + Verb-1?\r\nContoh:\r\n\r\nDo you eat rice?\r\n\r\nDoes she eat rice?', 1),
        ]
        for lesson_id, title, content, course_id in lessons:
            course = Course.objects.get(id=course_id)
            Lesson.objects.get_or_create(
                id=lesson_id,
                defaults={'title': title, 'content': content, 'course': course}
            )

        # Seed courses_quizresult
        quiz_results = [
            (92, 8, 10, 80, datetime.datetime(2025, 7, 17, 5, 47, 22, 161950, tzinfo=timezone.utc), 1, 2),
            (93, 7, 10, 70, datetime.datetime(2025, 7, 17, 5, 52, 52, 699652, tzinfo=timezone.utc), 2, 2),
            (94, 10, 10, 100, datetime.datetime(2025, 7, 17, 10, 39, 52, 720498, tzinfo=timezone.utc), 12, 2),
            (95, 10, 10, 100, datetime.datetime(2025, 7, 17, 13, 55, 9, 272719, tzinfo=timezone.utc), 2, 2),
            (96, 10, 10, 100, datetime.datetime(2025, 7, 17, 14, 18, 24, 281975, tzinfo=timezone.utc), 3, 2),
            (97, 10, 10, 100, datetime.datetime(2025, 7, 17, 14, 41, 58, 783976, tzinfo=timezone.utc), 4, 2),
        ]
        for quiz_id, score, total_questions, percentage, date_taken, course_id, user_id in quiz_results:
            course = Course.objects.get(id=course_id)
            user = User.objects.get(id=user_id)
            QuizResult.objects.get_or_create(
                id=quiz_id,
                defaults={
                    'score': score,
                    'total_questions': total_questions,
                    'percentage': percentage,
                    'date_taken': date_taken,
                    'course': course,
                    'user': user,
                }
            )

        # Seed django_content_type
        content_types = [
            (1, 'admin', 'logentry'),
            (3, 'auth', 'group'),
            (2, 'auth', 'permission'),
            (4, 'contenttypes', 'contenttype'),
            (8, 'courses', 'course'),
            (7, 'courses', 'lesson'),
            (13, 'courses', 'quiz'),
            (9, 'courses', 'quizresult'),
            (10, 'homework', 'homework'),
            (11, 'homework', 'homeworksubmission'),
            (12, 'homework', 'homeworktask'),
            (5, 'sessions', 'session'),
            (6, 'users', 'user'),
        ]
        for content_type_id, app_label, model in content_types:
            ContentType.objects.get_or_create(
                id=content_type_id,
                defaults={'app_label': app_label, 'model': model}
            )

        # Seed django_admin_log
        admin_logs = [
            (1, datetime.datetime(2025, 7, 7, 8, 53, 55, 983552, tzinfo=timezone.utc), '2', 'vicky', 2, '[{"changed": {"fields": ["Staff status", "Superuser status", "Role"]}}]', 6, 1),
            (2, datetime.datetime(2025, 7, 7, 8, 54, 3, 485853, tzinfo=timezone.utc), '1', 'josua123', 2, '[{"changed": {"fields": ["Role"]}}]', 6, 1),
            (3, datetime.datetime(2025, 7, 7, 9, 3, 51, 613692, tzinfo=timezone.utc), '1', 'josua123', 2, '[{"changed": {"fields": ["Role"]}}]', 6, 1),
            (4, datetime.datetime(2025, 7, 7, 9, 5, 6, 610797, tzinfo=timezone.utc), '1', 'Simple present tense', 1, '[{"added": {}}]', 8, 1),
            (5, datetime.datetime(2025, 7, 7, 9, 6, 40, 22156, tzinfo=timezone.utc), '1', 'Simple present tense', 2, '[]', 8, 1),
            (6, datetime.datetime(2025, 7, 7, 9, 6, 44, 451385, tzinfo=timezone.utc), '1', 'Simple present tense', 2, '[]', 8, 1),
            (7, datetime.datetime(2025, 7, 7, 9, 9, 39, 649724, tzinfo=timezone.utc), '1', 'Simple present tense - Daily Activities', 1, '[{"added": {}}]', 7, 1),
            (8, datetime.datetime(2025, 7, 8, 5, 17, 44, 917369, tzinfo=timezone.utc), '2', 'Simple past tense', 1, '[{"added": {}}]', 8, 1),
            (9, datetime.datetime(2025, 7, 8, 17, 1, 12, 313516, tzinfo=timezone.utc), '1', 'kak_ze', 2, '[{"changed": {"fields": ["Username"]}}]', 6, 1),
            (10, datetime.datetime(2025, 7, 8, 17, 1, 20, 764776, tzinfo=timezone.utc), '2', 'Vicky', 2, '[{"changed": {"fields": ["Username"]}}]', 6, 1),
            (11, datetime.datetime(2025, 7, 8, 17, 1, 29, 48548, tzinfo=timezone.utc), '1', 'Kak_Ze', 2, '[{"changed": {"fields": ["Username"]}}]', 6, 1),
            (12, datetime.datetime(2025, 7, 9, 8, 59, 38, 263844, tzinfo=timezone.utc), '3', 'Simple future tense', 1, '[{"added": {}}]', 8, 1),
            (13, datetime.datetime(2025, 7, 10, 3, 35, 9, 407408, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 1, '[{"added": {}}]', 10, 1),
            (14, datetime.datetime(2025, 7, 10, 3, 42, 54, 887451, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 2, '[{"added": {"name": "homework task", "object": "quiz - Selesaikan kuis \\u201cSim"}}]', 10, 1),
            (15, datetime.datetime(2025, 7, 10, 4, 35, 47, 549260, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 2, '[{"added": {"name": "homework task", "object": "upload - Buat kalimat \\u201cSimple"}}]', 10, 1),
            (16, datetime.datetime(2025, 7, 10, 4, 36, 2, 506871, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 2, '[]', 10, 1),
            (17, datetime.datetime(2025, 7, 10, 4, 36, 33, 61793, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 2, '[{"changed": {"fields": ["Assigned to"]}}]', 10, 1),
            (18, datetime.datetime(2025, 7, 10, 9, 19, 6, 468353, tzinfo=timezone.utc), '1', 'Latihan Simple Present', 2, '[{"changed": {"name": "homework task", "object": "quiz - Selesaikan kuis \\u201cSim", "fields": ["Quiz keyword"]}}]', 10, 1),
            (19, datetime.datetime(2025, 7, 10, 15, 58, 26, 781173, tzinfo=timezone.utc), '1', 'Latihan Simple present tense', 2, '[]', 10, 1),
            (20, datetime.datetime(2025, 7, 13, 19, 42, 4, 605050, tzinfo=timezone.utc), '2', 'Latihan Simple past tense', 1, '[{"added": {}}, {"added": {"name": "homework task", "object": "quiz - Selesaikan quiz ini "}}]', 10, 1),
            (21, datetime.datetime(2025, 7, 15, 8, 54, 20, 439445, tzinfo=timezone.utc), '2', 'Latihan Simple past tense', 2, '[{"changed": {"fields": ["Assigned to"]}}]', 10, 1),
            (22, datetime.datetime(2025, 7, 15, 8, 54, 26, 965491, tzinfo=timezone.utc), '1', 'Latihan Simple present tense', 2, '[{"changed": {"fields": ["Assigned to"]}}]', 10, 1),
            (23, datetime.datetime(2025, 7, 16, 10, 53, 54, 996495, tzinfo=timezone.utc), '11', 'Vicky - Buat kalimat “Simple', 2, '[{"changed": {"fields": ["Is approved"]}}]', 11, 1),
            (24, datetime.datetime(2025, 7, 16, 14, 21, 19, 95400, tzinfo=timezone.utc), '2', 'Latihan Simple past tense', 2, '[{"changed": {"fields": ["Assigned to"]}}]', 10, 1),
            (25, datetime.datetime(2025, 7, 16, 14, 21, 25, 157902, tzinfo=timezone.utc), '1', 'Latihan Simple present tense', 2, '[{"changed": {"fields": ["Assigned to"]}}]', 10, 1),
        ]
        for log_id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id in admin_logs:
            content_type = ContentType.objects.get(id=content_type_id)
            user = User.objects.get(id=user_id)
            LogEntry.objects.get_or_create(
                id=log_id,
                defaults={
                    'action_time': action_time,
                    'object_id': object_id,
                    'object_repr': object_repr,
                    'action_flag': action_flag,
                    'change_message': change_message,
                    'content_type': content_type,
                    'user': user,
                }
            )

        # Seed django_session
        sessions = [
            ('9voiyn80ig7exe9trqquemw0augx3821', '.eJxVjMsOwiAQRf-FtSHlMQO4dN9vIAOMUjU0Ke3K-O_apAvd3nPOfYlI21rj1nmJUxFnocTpd0uUH9x2UO7UbrPMc1uXKcldkQftcpwLPy-H-3dQqddvPTCloMEnQ0CgnfFGo8tusDqH5JiDDS6gN4RXndGCRVBKe_AmAyKL9we96jZv:1ub2Yz:4M90W0QmUJylsgYbccOVFxdZOsD-BNZnpB5YvoLiGAI', 
             datetime.datetime(2025, 7, 27, 19, 40, 41, 59537, tzinfo=timezone.utc)),
            ('y2l020vfr3ium5lazc0oxfvra9m5vv20', '.eJydVm1v2zgM_is8f1mLa5M06ZKsX4YmuQE73HAHrFgxrEMgW3SsxZZyktwsV_S_j7Rl56XZil6-JBIpis9D8lEeorkofTYvHdq5ktFV1I_OdvdikSxRs0F-E3phOonR3qq4wy6dYHWdD0ZiPgm-ewEy4TI6jcMLcZm-EYPBm3EcJ0M5TMaDsbyUPZm8Hl6OXvcHtBj0eiMZJ3E_HQ8vLvoXotcfjdJRbzSmoP-W6r95LpyfC-3WaF109UCb6LwymhZftiu68DZTSQYmBZ8hpCbPzVrpBcTkABJdQhjQVcaVVYWwG6B0G_9_LDrUHqYEVunSlA5uUDt8S2mYVbjvIbqme24MeJEvQcSm9JCJWHkHxoKlpdLoOnRkUvs118ICNVqRg7dEU-WdisRXrtMnIcnC91Ho1Qo1YxC-SrIwBedIKbsViiVbKJLHYmUs4wkHOeqsjmoxRfIwbczEFKscPUpQuuaC6O1Ej2dRTTEdm9LqgFi6X9XUJcZaTDw4QpL40jLTFgSsjFNe3SMwi6gTbOK_gNiPZfyNY_8O92hjOImFq8IXp7R17rrn6AK1W0_i9kQUXeW6wuJpe_ScuDkN5G6dpZJHgge2tm7UwN1MEJbGlzkioqxXiSL2TvfomhzS9U7leYM-zoVeXsFd9Jcxy9_gT5NpmNcfyIjSWC1xWwm7BKsWmQdt1p276ClDVsmWA0sDGBBSILIQ5ACFAPCGRP1cYbcTQ2x4VSDg9xVVzFXNoqp-KYzOq1mRsFY-e2lVP9N1aKXYhLz_IE43UK85-b9T6peQ-PVun-_lPjvMfZoZwznv9KTGhXhRD14dGe4MN0S_h7XwScYTdvOpHWi2UZvpV0_M08YsTWsNpllrUnLf9ssuqoZOmqBYLaK76D2IAgpEz7cXG0itYkGmIdfcO3cRKBrxzZFKvPevHI2qxUWZC1srV4Mt2PZ0qgEWbBJTpZWnqSmrwRfW0vuAXKoGZ-2pg9r8L7F5RyNJlzU71HeM83gVebBONqaELulRKTenlRixL34XxdtjEzQzwAcq933vQMQ1IWs9-OpDJ2ZkRkLy8zDMxGeyUqv8LMwvSz8NtO1VnrF-pHWjHoLafQ0xyQq50aCuEZekhongRy0j0Te5BKORh5jr5jKUxzUFhWw0hYWElrWSTINxV1R4-UzbsqS07RpGs9YP9-KXlvGXmrSMD4cewqqH6nxvBUkLkaByx2_kRa9HXbqwSN5TzJ0q2xf2wwacYiGqRc1UjycBpXav1DaAnChLo5RSvuE2t9w8-zoy4uqh4OekbXr3pHy32-rRi8xWS1yb_df9aI1yTl0H0PUCZUDGXVZv7T4A980mysP0v55F1f-09j_VF9rl0GfV92zn92Tn9zT6-vj4A9peY3k:1ucPo6:vQrxEoikXtYOBwXrKrXQPGEwNyoMGljQ5h97bURjjts', 
             datetime.datetime(2025, 7, 31, 14, 41, 58, 849721, tzinfo=timezone.utc)),
        ]
        for session_key, session_data, expire_date in sessions:
            Session.objects.get_or_create(
                session_key=session_key,
                defaults={'session_data': session_data, 'expire_date': expire_date}
            )

        # Seed homework_homework
        homeworks = [
            (1, 'Latihan Simple present tense', 'Latihan menulis kalimat dan menyelesaikan kuis tentang simple present.'),
            (2, 'Latihan Simple past tense', '-'),
        ]
        for homework_id, title, description in homeworks:
            Homework.objects.get_or_create(
                id=homework_id,
                defaults={'title': title, 'description': description}
            )

        # Seed homework_homeworktask
        homework_tasks = [
            (1, 'quiz', 'Selesaikan kuis “Simple Present Tense” di halaman kuis.', 'Simple present tense', 1, datetime.date(2025, 7, 11), datetime.datetime(2025, 7, 12, 15, 6, 38, 531923, tzinfo=timezone.utc)),
            (2, 'catatan', 'Buat kalimat “Simple Present Tense”.', None, 1, datetime.date(2025, 7, 11), datetime.datetime(2025, 7, 12, 15, 6, 38, 531923, tzinfo=timezone.utc)),
            (3, 'quiz', 'Selesaikan quiz ini untuk wawasan dasar mengenai simple past tense!', 'Simple past tense', 2, datetime.date(2025, 7, 18), datetime.datetime(2025, 7, 13, 19, 42, 4, 603462, tzinfo=timezone.utc)),
        ]
        for task_id, task_type, instruction, quiz_keyword, homework_id, deadline, posted_at in homework_tasks:
            homework = Homework.objects.get(id=homework_id)
            HomeworkTask.objects.get_or_create(
                id=task_id,
                defaults={
                    'task_type': task_type,
                    'instruction': instruction,
                    'quiz_keyword': quiz_keyword,
                    'homework': homework,
                    'deadline': deadline,
                    'posted_at': posted_at,
                }
            )

        # Seed homework_homeworksubmission
        homework_submissions = [
            (50, datetime.datetime(2025, 7, 17, 5, 42, 19, 392758, tzinfo=timezone.utc), 'homework_uploads/Copy_of_waisak_IG_DAjdhgk.jpg', 0, 1, 2, 1),
            (51, datetime.datetime(2025, 7, 17, 5, 42, 51, 737105, tzinfo=timezone.utc), 'homework_uploads/WhatsApp_Image_2025-07-14_at_21.18.44_57ef2d81.jpg', 0, 2, 2, 1),
            (52, datetime.datetime(2025, 7, 17, 5, 47, 22, 198751, tzinfo=timezone.utc), '', 1, 2, 1, 0),
            (53, datetime.datetime(2025, 7, 17, 5, 52, 52, 719608, tzinfo=timezone.utc), '', 1, 2, 3, 0),
        ]
        for submission_id, submitted_at, image, quiz_completed, student_id, task_id, is_approved in homework_submissions:
            student = User.objects.get(id=student_id)
            task = HomeworkTask.objects.get(id=task_id)
            HomeworkSubmission.objects.get_or_create(
                id=submission_id,
                defaults={
                    'submitted_at': submitted_at,
                    'image': image,
                    'quiz_completed': quiz_completed,
                    'student': student,
                    'task': task,
                    'is_approved': is_approved,
                }
            )

        # Seed homework_homework_assigned_to
        homework_assigned_to = [
            (6, 1, 1),
            (1, 1, 2),
            (5, 2, 1),
            (4, 2, 2),
        ]
        for assigned_id, homework_id, user_id in homework_assigned_to:
            homework = Homework.objects.get(id=homework_id)
            user = User.objects.get(id=user_id)
            homework.assigned_to.add(user)

        # Seed django_migrations (optional, as migrations are typically managed by Django)
        migrations = [
            (1, 'contenttypes', '0001_initial', datetime.datetime(2025, 7, 7, 8, 51, 47, 568970, tzinfo=timezone.utc)),
            (2, 'contenttypes', '0002_remove_content_type_name', datetime.datetime(2025, 7, 7, 8, 51, 47, 651522, tzinfo=timezone.utc)),
            (3, 'auth', '0001_initial', datetime.datetime(2025, 7, 7, 8, 51, 47, 984786, tzinfo=timezone.utc)),
            (4, 'auth', '0002_alter_permission_name_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 58334, tzinfo=timezone.utc)),
            (5, 'auth', '0003_alter_user_email_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 60094, tzinfo=timezone.utc)),
            (6, 'auth', '0004_alter_user_username_opts', datetime.datetime(2025, 7, 7, 8, 51, 48, 68380, tzinfo=timezone.utc)),
            (7, 'auth', '0005_alter_user_last_login_null', datetime.datetime(2025, 7, 7, 8, 51, 48, 75742, tzinfo=timezone.utc)),
            (8, 'auth', '0006_require_contenttypes_0002', datetime.datetime(2025, 7, 7, 8, 51, 48, 75742, tzinfo=timezone.utc)),
            (9, 'auth', '0007_alter_validators_add_error_messages', datetime.datetime(2025, 7, 7, 8, 51, 48, 91756, tzinfo=timezone.utc)),
            (10, 'auth', '0008_alter_user_username_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 98709, tzinfo=timezone.utc)),
            (11, 'auth', '0009_alter_user_last_name_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 98709, tzinfo=timezone.utc)),
            (12, 'auth', '0010_alter_group_name_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 123219, tzinfo=timezone.utc)),
            (13, 'auth', '0011_update_proxy_permissions', datetime.datetime(2025, 7, 7, 8, 51, 48, 123219, tzinfo=timezone.utc)),
            (14, 'auth', '0012_alter_user_first_name_max_length', datetime.datetime(2025, 7, 7, 8, 51, 48, 139193, tzinfo=timezone.utc)),
            (15, 'users', '0001_initial', datetime.datetime(2025, 7, 7, 8, 51, 48, 516635, tzinfo=timezone.utc)),
            (16, 'admin', '0001_initial', datetime.datetime(2025, 7, 7, 8, 51, 48, 684200, tzinfo=timezone.utc)),
            (17, 'admin', '0002_logentry_remove_auto_add', datetime.datetime(2025, 7, 7, 8, 51, 48, 693750, tzinfo=timezone.utc)),
            (18, 'admin', '0003_logentry_add_action_flag_choices', datetime.datetime(2025, 7, 7, 8, 51, 48, 693750, tzinfo=timezone.utc)),
            (19, 'sessions', '0001_initial', datetime.datetime(2025, 7, 7, 8, 51, 48, 754954, tzinfo=timezone.utc)),
            (20, 'courses', '0001_initial', datetime.datetime(2025, 7, 7, 9, 2, 39, 647609, tzinfo=timezone.utc)),
            (21, 'courses', '0002_quizresult', datetime.datetime(2025, 7, 7, 16, 5, 51, 983643, tzinfo=timezone.utc)),
            (22, 'homework', '0001_initial', datetime.datetime(2025, 7, 10, 2, 53, 15, 699801, tzinfo=timezone.utc)),
            (23, 'homework', '0002_homework_assigned_to', datetime.datetime(2025, 7, 10, 3, 28, 18, 483611, tzinfo=timezone.utc)),
            (24, 'homework', '0003_homeworktask_deadline', datetime.datetime(2025, 7, 10, 16, 23, 5, 76835, tzinfo=timezone.utc)),
            (25, 'homework', '0004_remove_homework_deadline', datetime.datetime(2025, 7, 10, 17, 22, 41, 834256, tzinfo=timezone.utc)),
            (26, 'homework', '0005_homeworktask_posted_at_alter_homeworktask_task_type', datetime.datetime(2025, 7, 12, 15, 6, 38, 689969, tzinfo=timezone.utc)),
            (27, 'homework', '0006_remove_homework_created_at', datetime.datetime(2025, 7, 12, 15, 6, 38, 768137, tzinfo=timezone.utc)),
            (28, 'courses', '0003_course_uuid', datetime.datetime(2025, 7, 15, 15, 13, 25, 124522, tzinfo=timezone.utc)),
            (29, 'homework', '0007_homeworksubmission_is_approved', datetime.datetime(2025, 7, 16, 10, 33, 21, 256085, tzinfo=timezone.utc)),
            (30, 'courses', '0003_quiz', datetime.datetime(2025, 7, 16, 13, 33, 51, 897447, tzinfo=timezone.utc)),
            (31, 'courses', '0004_quiz_quiz_json', datetime.datetime(2025, 7, 16, 14, 2, 33, 272971, tzinfo=timezone.utc)),
            (32, 'courses', '0005_delete_quiz', datetime.datetime(2025, 7, 16, 14, 24, 48, 714824, tzinfo=timezone.utc)),
        ]
        # Note: django_migrations is typically managed by Django, so seeding it is optional and may not be necessary.
        # If needed, you can insert into django_migrations table using raw SQL or a similar approach.

        self.stdout.write(self.style.SUCCESS("Database seeding completed successfully!"))