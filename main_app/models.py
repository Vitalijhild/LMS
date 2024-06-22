from django.db import models
from accounts.models import CustomUser, Course

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Lesson(models.Model):
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class Task(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='tasks', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class AnswerVariant(models.Model):
    task = models.ForeignKey(Task, related_name='answer_variants', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class TaskProgress(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='progresses')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='task_progresses')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.task.title} - {'Completed' if self.completed else 'Incomplete'}"

class LessonProgress(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progresses')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='lesson_progresses')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.lesson.title} - {'Completed' if self.completed else 'Incomplete'}"
