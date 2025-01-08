from django.views.generic import ListView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = 'title'
    template_title = "Posts.html"
    context_object_name = "Post"