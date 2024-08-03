from django.views.generic import View, TemplateView, ListView, DetailView
from .models import *
from django.shortcuts import render, redirect

class CourseListView(ListView):
    model = Course
    template_name = 'main_app/course_list.html'
    paginate_by = 5
    context_object_name = 'courses'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'main_app/course_detail.html'
    context_object_name = 'course'