from django.shortcuts import render

posts = [
    {
        'author': "Antonio Dottori",
        'title': "How to create a blog post 101",
        'content': "First post here.",
        'date_posted': "February 04, 2021"
    },
    {
        'author': "João da Silva",
        'title': "Posting on blogs",
        'content': "Second post here.",
        'date_posted': "March 05, 2021"
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    return render(request, "blog/about.html", {"title": "about"})


# outra forma de criar a rota
# def home(request):
#    return HttpResponse("<h1>Blog Home</h1>")