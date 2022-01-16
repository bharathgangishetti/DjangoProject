from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author' : 'Bharath',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'January 16 2022'
    },

    {
        'author' : 'Gangishetti',
        'title' : 'Blog Post 2',
        'content' : 'second Post Content',
        'date_posted' : 'January 16 2022'
    }
]




def home(request):
    context = {
        'posts' : posts,
        'title' : 'Blog'
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title' : 'about'})


# Create your views here.
