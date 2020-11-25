from rest_framework import routers, serializers, viewsets

from accounts.models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','avatar','phone','password','first_name','last_name','dob')



