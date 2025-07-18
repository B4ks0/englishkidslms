from django.core.management.base import BaseCommand
from courses.models import Course

TENSES = [
    {
        "name": "Simple Present Tense",
        "description": "Digunakan untuk menyatakan kebiasaan, fakta, atau kejadian yang terjadi berulang-ulang.",
    },
    {
        "name": "Present Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang sedang berlangsung saat ini.",
    },
    {
        "name": "Present Perfect Tense",
        "description": "Digunakan untuk menyatakan aksi yang telah selesai pada waktu yang tidak spesifik di masa lalu.",
    },
    {
        "name": "Present Perfect Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang telah dimulai di masa lalu dan masih berlangsung hingga sekarang.",
    },
    {
        "name": "Simple Past Tense",
        "description": "Digunakan untuk menyatakan aksi yang terjadi dan selesai di masa lalu.",
    },
    {
        "name": "Past Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang sedang berlangsung di masa lalu.",
    },
    {
        "name": "Past Perfect Tense",
        "description": "Digunakan untuk menyatakan aksi yang telah selesai sebelum aksi lain di masa lalu.",
    },
    {
        "name": "Past Perfect Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang telah berlangsung sebelum aksi lain di masa lalu.",
    },
    {
        "name": "Simple Future Tense",
        "description": "Digunakan untuk menyatakan aksi yang akan terjadi di masa depan.",
    },
    {
        "name": "Future Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang akan sedang berlangsung di masa depan.",
    },
    {
        "name": "Future Perfect Tense",
        "description": "Digunakan untuk menyatakan aksi yang akan telah selesai di masa depan.",
    },
    {
        "name": "Future Perfect Continuous Tense",
        "description": "Digunakan untuk menyatakan aksi yang akan telah berlangsung selama periode waktu tertentu di masa depan.",
    },
]

class Command(BaseCommand):
    help = "Seed all English tenses into Course model"

    def handle(self, *args, **kwargs):
        for tense in TENSES:
            obj, created = Course.objects.get_or_create(
                name=tense["name"],
                defaults={
                    "description": tense["description"],
                    "teacher_id": 1,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created: {tense['name']}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {tense['name']}")) 