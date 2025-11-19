from django.contrib import admin
from django.urls import path
from accounts.views import SignupView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',SignupView.as_view())
]
