from django.urls import path
from chatbot.views import chatbot_view

app_name = "chatbot"

urlpatterns = [
    path("", chatbot_view, name="chatbot"),
]
