from rest_framework import serializers
from .models import Pattern


class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = '__all__'
a = 42
