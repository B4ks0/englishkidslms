from django.contrib import admin
from .models import Homework, HomeworkTask, HomeworkSubmission

class HomeworkTaskInline(admin.TabularInline):
    model = HomeworkTask
    extra = 1

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('assigned_to',)  # <--- supaya bisa pilih banyak murid
    inlines = [HomeworkTaskInline]

admin.site.register(HomeworkTask)
admin.site.register(HomeworkSubmission)