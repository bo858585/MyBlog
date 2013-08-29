# coding: utf-8

from django.core.urlresolvers import reverse
from django.test import TestCase

from .models import Post
from .views import PostCreate

import json


class PostTest(TestCase):

    def setUp(self):
        """
        Creates two posts in blog and gets two urls:
        url of the posts list and url of the post creating
        """
        Post.objects.get_or_create(title=u"A title 1", text=u"A text 1")
        Post.objects.get_or_create(title=u"A title 2", text=u"A text 2")

        self.posts_list_url = reverse("blog_posts")
        self.post_to_blog = reverse("post_to_blog")

    def test_list(self):
        """
        Gets posts list and checks that posts have initial title and text
        """
        response = self.client.get(self.posts_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, u"A title 1")
        self.assertContains(response, u"A title 2")
        self.assertContains(response, u"A text 1")
        self.assertContains(response, u"A text 2")

    def test_create(self):
        """
        Creates post and checks that it exists after creating
        """
        post = {"title": "A title 3", "text": "A text 3"}
        response = self.client.post(self.post_to_blog, post, follow=True)
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, u"A title 3")
        self.assertContains(response, u"A text 3")
