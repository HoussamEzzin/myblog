from django.shortcuts import render


# just for testing : 
posts = [
    {
        'author' : 'Ezzin',
        'title' : 'first post',
        'content': 'this is my first post',
        'date_posted': 'October 07, 2021'
    },
    {
        'author' : 'Ezzin',
        'title' : 'second post',
        'content': 'this is my second post',
        'date_posted': 'October 08, 2021'
    },
]


def home(request):
    context = {
        'posts' : posts,
        'title': 'HomePage'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title' : 'About'
    }
    return render(request, 'blog/about.html', context)