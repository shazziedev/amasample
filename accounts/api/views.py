
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .serializer import *
from accounts.models import *

class UserListView(ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class myProfile(RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer