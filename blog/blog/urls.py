# coding: utf-8

from django.conf.urls import patterns, url
from django.views.generic.dates import ArchiveIndexView

from .models import Post
from .views import PostCreate

urlpatterns = patterns('blog.blog.views',
                       # Adds post to the blog
                       url(r'^post/$',
                           PostCreate.as_view(model=Post),
                           name="post_to_blog"
                           ),

                       # Blog posts list
                       url(r'^$',
                           ArchiveIndexView.as_view(
                               model=Post,
                               date_field="publication_date"),
                           name="blog_posts"
                           ),
                       )
