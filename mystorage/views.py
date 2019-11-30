from rest_framework import viewsets
from .models import Essay
from .serializers import EssaySerializer
from rest_framework.filters import SearchFilter


class PostViewSet(viewsets.ModelViewSet):

    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    # 검색기능
    filter_backends = [SearchFilter]
    search_fields = ('title', 'contents', 'pub_date')
