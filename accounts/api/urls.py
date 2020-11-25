from django.urls import path,include

from .views import *

urlpatterns = [
	path('', UserListView.as_view()),
	path('<pk>/', myProfile.as_view()),
]