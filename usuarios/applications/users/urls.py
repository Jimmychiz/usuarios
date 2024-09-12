from . import views
from django.urls import path

app_name="users_app"

urlpatterns = [
    path(
        "Register/",
        views.UserRegisterView.as_view(),
        name="user-register"

    )
]
