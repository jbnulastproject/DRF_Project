from .models import Essay
from rest_framework import serializers


class EssaySerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Essay
        fields = ('pk', 'title', 'contents', 'pub_date', 'author_name')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
