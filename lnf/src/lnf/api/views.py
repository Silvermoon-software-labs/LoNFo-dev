from rest_framework.generics import ListAPIView
from lnf.models import LostNFound
from lnf.api.serialzers import PostSerializer

class PostListAPIView(ListAPIView):
    queryset =LostNFound.objects.all()
    serializer_class = PostSerializer
