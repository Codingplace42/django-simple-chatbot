# Django Simple Chatbot

It's a very basic Chatbot for Python Django including NLTK and 
Django-REST-framework. This Chatbot is currently working without
Machine learning algorithms. Decisions are made by simple statistic evaluation.

The Algorithm is based on labeled data on your Django Database and the tool
is supporting continuous labeling.

## Requirements
- Python (3.7, 3.8, 3.9)
- Django (2.2, 3.0, 3.1, 3.2)

## Dependencies
- [Django REST-Framework - Awesome web-browsable Web APIs.](https://www.django-rest-framework.org)
- [NLTK - the Natural Language Toolkit](https://www.nltk.org)

## Installation

Install using `pip` ...

```
pip install django-simple-chatbot
```

add `simple_chatbot` to your `INSTALLED_APPS` setting.

```
INSTALLED_APPS = [
    ...,
    'simple_chatbot'
]
```

**Note:** Make sure to run `manage.py migrate` after changing your settings.
The simple_chatbot app provides Django database migrations.

## Quickstart

Create a `response.py` file inside of an already installed app.
```
from simple_chatbot.responses import GenericRandomResponse


class GreetingResponse(GenericRandomResponse):
    choices = ("Hey, how can I help you?",
               "Hey friend. How are you? How can I help you?")


class GoodbyeResponse(GenericRandomResponse):
    choices = ("See you later.",
               "Thanks for visiting.",
               "See ya! Have a nice day.")
```

Add this Response to your `SIMPLE_CHATBOT` setting
```
SIMPLE_CHATBOT = {
    ...
    'responses': (
        ("YOUR_APP.responses.GreetingResponse", "Greeting"),
        ("YOUR_APP.responses.GoodbyeResponse", "Goodbye"),
    ),
}
```

Go to your Django admin and create `greeting` and `goodbye` tags.
Your response options will be selectable via choices.

Go to your Django admin, write some patterns and label them. You can just use
the following labels:
```
[Greeting]
"Hi, how are you?", "Is anyone there?", "Hello", "What's up?!", "hey there!"

["Goodbye"]
"Bye", "See you later", "Goodbye", "I need to go now."
```
**Note** If you do not want to write that patterns by yourself, use a command
`manage.py simple_chatbot_initial`. You need to label them after initializing.

The package will automatically tokenize the input and map tokens to labels.

Add simple_chatbot url to your routings:
```
from simple_chatbot.views import SimpleChatbot

urlpatterns = [
    ...
    path("simple_chatbot/", SimpleChatbot.as_view())
]
```

Make a Post request to your new endpoint:
```
curl \
    -H "Content-Type: application/json" \
    --data '{"message":"how r u?"}' \
    http://localhost:8000/simple_chatbot/
```

The response should look like
```
{
    "tag": "Greeting",
    "message": "Hey, how can I help you?"
}
```

## Raw Documentation

### Database Models
- `Pattern` - message which might be send by a user. Add a tag to the pattern
    for being able to identify and response to that message
- `Tag` - includes information about Response class for a specific method
- `Token` - tokenized words which are referencing to different patterns. The
    user-input will be identified by different tokens.
- `UserMessageInput` - new inputs from production. It contains information
    about chosen pattern. You can label that messages later and include them
    into the system.

### settings options
You can add following options to your `SIMPLE_CHATBOT` setting:
- STEMMER_MODULE: nltk package for stumming your strings - 
    default: `nltk.stem.lancaster.LancasterStemmer`.
- responses: choices for your tags. It should reference to a response class.
    **Warning** You won't be able to create tags without response classes.

### Response Classes
The `simple_chatbot.responses` package provides currently following response classes:
- BaseResponse
- GenericRandomResponse

#### BaseResponse
It's just an abstract class for require a specific shape of your response
classes. If you are creating a new response, you should inheritance from that
class.

#### GenericRandomResponse
It will choose a generic answer from class property `choices`.

### Views
This `simple_chatbot.responses` includes a single view `SimpleChatbot`.
This view is reusable. The most important changeble option:
- `save_pattern`: if True each message will be saved and you can post label
    the incoming messages. default `True`.

#### SimpleChatbot API Documentation
- Required Request type: `POST`
- payload: `{message: "YOUR MESSAGE"}`
- response: `{tag: 'TAG', message: 'RESPONSE'}`

## About
It's a very basic Chatbot decisions are made with tools by NLTK which follows
basic preprocessing for NLP of tokenization and stumming.

This package is inspired by the Chatbot Tutorial of Tech witch Tim.
Checkout his blog: https://www.techwithtim.net/tutorials/ai-chatbot/

In my opinion the used script is teaching important concepts but it's 
overtooled by using Deep-Learning algorithm on that small amount of data.

Real NLP's and Deep Learning algorithms needs a large amount of data. One
problem in smaller and beginning projects: You won't have that amount of data
by starting your projects. 

**This package gives you possibilities to work with a small amount of data and
it helps you to collect new data for being able to use deep learning
algorithms one day.**

### Contributing
Fork the repo and get stuck in!
