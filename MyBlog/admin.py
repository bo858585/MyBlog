"""
Register blog Post model at the admin
"""

# coding: utf-8

from django.contrib import admin
from blog.models import Post

admin.site.register(Post)
