from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from .models import Pattern, Tag
from .serializers import ChatResponseSerializer, UserMessageInputSerializer


class SimpleChatbot(GenericAPIView):
    save_pattern = True
    queryset = Pattern.objects
    serializer_class = ChatResponseSerializer

    def perform_create(self, serializer, identified_tag):
        serializer.save(identified_tag=identified_tag)

    def get_tag(self, string):
        return Tag.objects.get_tag_by_string(string)

    def get_response_module(self, tag):
        module = tag.method.split(".")
        mod = __import__(".".join(module[:-1]), fromlist=module[-1])
        return getattr(mod, module[-1])

    def evaluate_message(self, request, *args, **kwargs):
        message_serializer = UserMessageInputSerializer(data=request.data)
        message_serializer.is_valid(raise_exception=True)
        tag = self.get_tag(request.data["message"])
        klass = self.get_response_module(tag)()
        response = klass.get_response()
        if self.save_pattern:
            self.perform_create(message_serializer, tag)
        data = {"tag": tag.get_method_display(), "message": response}
        serializer = self.get_serializer(data)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        return self.evaluate_message(request, *args, **kwargs)
