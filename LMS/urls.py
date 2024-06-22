from django.contrib import admin
from django.urls import path, include
from main_app.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('main_app.urls')),
    path('', HomePageView.as_view(), name='home'),
]
