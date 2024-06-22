from django.contrib import admin
from .models import Module, Lesson, Task, AnswerVariant, TaskProgress, LessonProgress

class ModuleInline(admin.StackedInline):
    model = Module
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class AnswerVariantInline(admin.StackedInline):
    model = AnswerVariant
    extra = 3

class TaskInline(admin.StackedInline):
    model = Task
    extra = 1

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [AnswerVariantInline]
    list_display = ('title', 'lesson', 'user', 'due_date')

@admin.register(AnswerVariant)
class AnswerVariantAdmin(admin.ModelAdmin):
    list_display = ('text', 'task', 'is_correct')

@admin.register(TaskProgress)
class TaskProgressAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'completed')

@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'user', 'completed')
