from django.urls import path
from .views import ReceiveMessageView

urlpatterns = [
    path('external_user_message/', ReceiveMessageView.as_view(),
         name='external_user_message')
]
