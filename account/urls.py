from django.urls import path
from . import views
urlpatterns = [
    path("register/",views.Signup),
    path("login/",views.Login),
    path("messages/",views.SendMessageView.as_view()),


]