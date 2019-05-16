from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_blank=True, max_length=100)
    body = serializers.CharField(required=True, allow_blank=True)

    def create(self, validated_data):
        return News.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance