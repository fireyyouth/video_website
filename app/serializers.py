from rest_framework import serializers
from main.models import Preview

class PreviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preview
        fields = ['title', 'img']