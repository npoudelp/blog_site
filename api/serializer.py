from rest_framework import serializers
from api.models import Posts

class Post(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Posts