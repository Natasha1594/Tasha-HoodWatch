from django import test
from django.test import TestCase
from .models import NeighbourHood, Profile, Business, Post
from django.contrib.auth.models import User
from django.contrib import auth

class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='natasha')
        self.user.save()

        self.profile_test = Profile(id=1, name='image', profile_picture='default.jpg', bio='this is a test profile',
                                user=self.user)


    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_method(self):
        self.save_profile()
        editors = Profile.objects.all()
        self.assertTrue(len(editors) > 0)

class TestPost(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='natasha', user=User(username='natasha1594'))
        

        self.image_test = Post(image='default.png', name='test', user=self.profile_test)

    def test_insatance(self):
        self.assertTrue(isinstance(self.image_test, Post))

    def test_save_image(self):
        self.image_test.save_image()
        images = Post.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)