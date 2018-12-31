from rest_framework import serializers
from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        # fields = ('title', 'body', 'result', 'feedback', 'last_modify_date', 'created')