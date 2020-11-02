from django.shortcuts import render
from django.http import HttpResponse

# dummy data
posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': '02.11.2020'
    },
    {
        'author': 'Jane Dow',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': '03.11.2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})










