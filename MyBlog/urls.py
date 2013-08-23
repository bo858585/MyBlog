"""
The controller of the project applications
"""

# coding: utf-8

from django.conf.urls import patterns, include, url
from .models import Post
from django.views.generic.dates import ArchiveIndexView
from .views import PostCreate


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
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

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       )
