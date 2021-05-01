from rest_framework.generics import GenericAPIView
from .models import Pattern, Tag


class SimpleChatbot(GenericAPIView):
    save_pattern = True
    queryset = Pattern.objects

    def get(self, request, *args, **kwargs):
        s = "What is your recommendation for today?"
        tag = Tag.objects.get_tag_by_string(s)
        return {}
