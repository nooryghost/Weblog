from django.urls import path, include

from .views import SignupView

urlpatterns =[
    path("login/", include("django.contrib.auth.urls")),
    path("signup/", SignupView.as_view())
]