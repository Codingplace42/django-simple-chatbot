from django.http import HttpResponse
from .tokenizer import get_tokens_from_pattern


def dashboard(request):
    get_tokens_from_pattern("HELLO WORLD")
    return HttpResponse("Chatbot")
