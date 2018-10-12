from rest_framework.generics import ListAPIView
from lnf.models import LostNFound
class PostListAPIView(ListAPIView):
    queryset = LostNFound.objects.all()