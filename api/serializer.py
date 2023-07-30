from rest_framework import serializers
from api.models import Posts

class Post_form(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Posts