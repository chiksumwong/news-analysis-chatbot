from rest_framework import serializers

from chatbot.models import Record


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
            model = Record
            fields = '__all__'