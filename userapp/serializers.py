from rest_framework.serializers import ModelSerializer
from .models import CustomUser
class ListDetailSerailizer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields =['id','email','username']