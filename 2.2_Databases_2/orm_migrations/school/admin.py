from django.contrib import admin

from .models import Student, Teacher, Schedule


class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 1


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group', )
    inlines = [ScheduleInline, ]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject', )
    inlines = [ScheduleInline, ]
