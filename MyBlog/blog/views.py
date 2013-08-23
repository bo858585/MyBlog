from django.views.generic.edit import CreateView

from .models import Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'publicaton_date', 'text']
