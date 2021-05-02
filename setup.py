import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-simple-chatbot",
    version="0.0.4",
    author="Janga",
    license='MIT License',
    author_email="jangascodingplace@gmail.com",
    description="A very basic Django Chatbot ft. NLTK and DRF",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Codingplace42/django-simple-chatbot",
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'django>=2.2',
        'nltk',
        'djangorestframework'
    ]
)
