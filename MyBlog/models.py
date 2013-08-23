"""
The model of the blog Post
"""

# coding: utf-8

from django.core.urlresolvers import reverse
from django.db import models


class Post(models.Model):

    """
    Blog post
    """

    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)
    publication_date = models.DateTimeField(
        auto_now_add=True
    )

    def get_absolute_url(argument):
        """
        The url of the post
        """
        return '/'

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["title", "publication_date", "text"]
