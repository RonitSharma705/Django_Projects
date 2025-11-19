from django.contrib import admin
from django.urls import path
from accounts.views import SignupView,LoginView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignupView.as_view()),
    path('login/',SignupView.as_view())
]
