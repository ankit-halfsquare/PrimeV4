from rest_framework import serializers
from core.models import (
    View,Task,Project,ViewField
) 


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'


class ViewFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewField
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'