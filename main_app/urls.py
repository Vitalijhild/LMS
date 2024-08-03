from django.urls import path
from .views import *

urlpatterns = [
    path('course_list/', CourseListView.as_view(), name='course-list'),
    path('course_detail/<int:pk>', CourseDetailView.as_view(), name='course-detail')

]